def _validate_input(prices, discount_rate):
    if not isinstance(prices, (list, tuple)):
        raise TypeError("Prices must be a list or tuple.")
    if len(prices) == 0:
        raise ValueError("Prices list cannot be empty.")
    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be numeric.")
    if discount_rate < 0 or discount_rate >= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

def apply_discount(prices, discount_rate):
    _validate_input(prices, discount_rate)
    factor = 1.0 - discount_rate
    return tuple(price * factor for price in prices)

if __name__ == '__main__':
    values = (100, 200, 300)
    rate = 0.05
    output = apply_discount(values, rate)
    print(output)