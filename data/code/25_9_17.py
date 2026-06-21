class PricingError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeValueError(PricingError):
    def __init__(self):
        super().__init__("Values cannot be negative.")

class ExcessiveDiscountError(PricingError):
    def __init__(self):
        super().__init__("Discount cannot exceed 100 percent.")

def get_final_price(base_price: float, percent_off: float) -> float:
    if base_price < 0:
        raise NegativeValueError()
    if percent_off < 0:
        raise NegativeValueError()
    if percent_off > 100:
        raise ExcessiveDiscountError()
    
    multiplier = 1 - (percent_off / 100)
    return base_price * multiplier

if __name__ == '__main__':
    price_a = 150.0
    disc_a = 10.0
    print(get_final_price(price_a, disc_a))
    
    price_b = 0.0
    disc_b = 50.0
    print(get_final_price(price_b, disc_b))
    
    price_c = 200.0
    disc_c = 100.0
    print(get_final_price(price_c, disc_c))