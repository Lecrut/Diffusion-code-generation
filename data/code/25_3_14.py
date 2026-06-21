def _validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Price must be a number")
    if value < 0:
        raise ValueError("Price cannot be negative")
    return True

def apply_discount(price):
    _validate_price(price)
    if price > 100:
        return price * 0.9
    return price * 0.95

if __name__ == '__main__':
    test_values = [50, 150]
    for value in test_values:
        print(apply_discount(value))