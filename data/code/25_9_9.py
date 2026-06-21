class InvalidPriceError(Exception):
    def __init__(self):
        super().__init__("Price must be non-negative")

class InvalidDiscountError(Exception):
    def __init__(self):
        super().__init__("Discount must be between 0 and 100")

def apply_discount(base_price: float, discount_rate: float) -> float:
    if base_price < 0:
        raise InvalidPriceError()
    if discount_rate < 0 or discount_rate > 100:
        raise InvalidDiscountError()
    multiplier = (100 - discount_rate) / 100
    return base_price * multiplier

if __name__ == '__main__':
    test_price = 250.50
    test_discount = 15
    final = apply_discount(test_price, test_discount)
    print(final)
    zero_discount = apply_discount(100, 0)
    print(zero_discount)
    full_discount = apply_discount(100, 100)
    print(full_discount)