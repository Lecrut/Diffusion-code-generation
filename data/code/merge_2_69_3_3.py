from typing import Union
def validate_positive(value: float) -> bool:
    return isinstance(value, (int, float)) and value > 0
def grams_to_pounds(grams: int) -> str:
    if not validate_positive(grams):
        raise ValueError("Input must be a positive number.")
    pounds = grams * 0.00220462
    return f"{pounds:.5f} lbs"
def kilograms_to_ounces(kg: int) -> str:
    if not validate_positive(kg):
        raise ValueError("Input must be a positive number.")
    ounces = kg * 35.274
    return f"{ounces:.5f} oz"
def pounds_to_kilograms(pounds: float) -> str:
    if not (isinstance(pounds, (int, float)) and pounds >= 0):
        raise ValueError("Input must be a non-negative number.")
    kilograms = pounds * 0.453592
    return f"{kilograms:.6f} kg"
def ounces_to_grams(ounces: int) -> str:
    if not validate_positive(ounces):
        raise ValueError("Input must be a positive number.")
    grams = ounces * 28.3495
    return f"{grams:.5f} g"
if __name__ == '__main__':
    print(grams_to_pounds(100))
    print(kilograms_to_ounces(2))
    print(pounds_to_kilograms(5))
    print(ounces_to_grams(8))