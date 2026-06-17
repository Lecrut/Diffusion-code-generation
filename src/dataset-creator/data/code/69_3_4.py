from typing import Union
def validate_positive(value: float) -> bool:
    return isinstance(value, (int, float)) and value > 0
def grams_to_pounds(grams: float) -> float:
    if not validate_positive(grams):
        raise ValueError("Input must be a positive number.")
    return grams * 0.00220462
def kilograms_to_ounces(kg: float) -> float:
    if not validate_positive(kg):
        raise ValueError("Input must be a positive number.")
    return kg * 35.274
    def pounds_to_kilograms(pounds: float) -> float:
        if not validate_positive(pounds):
            raise ValueError("Input must be a positive number.")
        return pounds / 0.00220462
def ounces_to_grams(ounces: float) -> float:
    if not validate_positive(ounces):
        raise ValueError("Input must be a positive number.")
    return ounces * 35.274
if __name__ == '__main__':
    sample_g = 1000
    result_pounds = grams_to_pounds(sample_g)
    print(f"{sample_g}g is {result_pounds:.6f}lbs")