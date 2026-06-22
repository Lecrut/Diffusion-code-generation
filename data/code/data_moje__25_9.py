class PriceError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativePriceError(PriceError):
    def __init__(self):
        super().__init__("Original price cannot be negative.")

class NegativeDiscountError(PriceError):
    def __init__(self):
        super().__init__("Discount percentage cannot be negative.")

class DiscountOverHundredError(PriceError):
    def __init__(self):
        super().__init__("Discount percentage cannot exceed 100%.")

class InvalidInputError(PriceError):
    def __init__(self, message):
        super().__init__(message)

def calculate_final_price(original_price: float, discount_percentage: float) -> float:
    if not isinstance(original_price, (int, float)):
        raise InvalidInputError("Original price must be a number.")
    if not isinstance(discount_percentage, (int, float)):
        raise InvalidInputError("Discount percentage must be a number.")
    if original_price < 0:
        raise NegativePriceError()
    if discount_percentage < 0:
        raise NegativeDiscountError()
    if discount_percentage > 100:
        raise DiscountOverHundredError()
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return final_price

if __name__ == '__main__':
    result1 = calculate_final_price(100, 20)
    print(result1)

    result2 = calculate_final_price(50, 50)
    print(result2)

    try:
        calculate_final_price(-10, 10)
    except NegativePriceError as e:
        print(str(e))

    try:
        calculate_final_price(100, -5)
    except NegativeDiscountError as e:
        print(str(e))

    try:
        calculate_final_price(100, 150)
    except DiscountOverHundredError as e:
        print(str(e))

    try:
        calculate_final_price("abc", 10)
    except InvalidInputError as e:
        print(str(e))