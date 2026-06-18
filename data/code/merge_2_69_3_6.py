from typing import Union
def grams_to_pounds(grams: float) -> float:
    if not isinstance(grams, (int, float)):
        raise TypeError("Input must be a number.")
    return grams * 0.00220462
def kilograms_to_ounces(kg: Union[int, float]) -> float:
    if not isinstance(kg, (int, float)):
        raise TypeError("Input must be a number.")
    return kg * 35.274
if __name__ == '__main__':
    sample_grams = 1000
    result_g_to_lb = grams_to_pounds(sample_grams)
    sample_kg = 5
    result_kg_to_oz = kilograms_to_ounces(sample_kg)