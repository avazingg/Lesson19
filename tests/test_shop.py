import pytest

from src.shop import Shop

@pytest.fixture()
def my_shop():
    return Shop()

@pytest.mark.parametrize("item, quantity, expected" , [
    ("Apple", 2, {"Apple": 2}),
    ("Peanut", 3, {"Peanut": 3}),
    ("Lemon", 0, ValueError)
])

def test_add_to_cart(my_shop, item, quantity, expected):
    if quantity > 0:
        assert my_shop.add_to_cart(item, quantity) == expected
    else:
        with pytest.raises(ValueError):
            my_shop.add_to_cart(item,quantity)

@pytest.fixture()
def prices():
    prices_of_items = {
        "Coke" : 2,
        "Sugar": 3,
        "Cauliflower" : 5
    }
    return prices_of_items

def test_calculate_total(my_shop, prices):
    my_shop.add_to_cart(item="Coke", quantity=2)
    my_shop.add_to_cart(item="Sugar", quantity=1)
    my_shop.add_to_cart(item="Cauliflower", quantity=5)
    assert my_shop.calculate_total(prices) == 32

@pytest.mark.parametrize("total, discount, expected" , [
    (32, 50, 16),
    (40, 20, 32),
    (1, 1000, ValueError)
])
def test_apply_discount(my_shop, total, discount,expected):
    if 0 < discount < 100:
        assert my_shop.apply_discount(total, discount) == expected
    else:
        with pytest.raises(ValueError):
            my_shop.apply_discount(total,discount)

