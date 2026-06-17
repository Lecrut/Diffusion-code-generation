from typing import Union
def convert_grams_to_pounds(grams: float) -> float:
    if not isinstance(grams, (int, float)):
        raise TypeError("Input must be a number.")
    if grams < 0:
        raise ValueError("Grams cannot be negative.")
    return grams * 0.00220462
def convert_kilograms_to_ounces(kg: Union[int, float]) -> float:
    if not isinstance(kg, (int, float)):
        raise TypeError("Input must be a number.")
    if kg < 0:
        raise ValueError("Kilograms cannot be negative.")
    return kg * 35.274
def convert_pounds_to_kilograms(pounds: Union[int, float]) -> float:
    if not isinstance(pounds, (int, float)):
        raise TypeError("Input must be a number.")
    if pounds < 0:
        raise ValueError("Pounds cannot be negative.")
    return pounds * 0.453592
def convert_ounces_to_kilograms(ounces: Union[int, float]) -> float:
    if not isinstance(ounces, (int, float)):
        raise TypeError("Input must be a number.")
    if ounces < 0:
        raise ValueError("Ounces cannot be negative.")
    return ounces * 0.0283495
if __name__ == '__main__':
    sample_grams = 1000
    result_g_to_lb = convert_grams_to_pounds(sample_grams)
    sample_kg = 5
    result_kg_to_oz = convert_kilograms_to_ounces(sample_kg)
    print(f"{sample_grams} grams is {result_g_to_lb:.4f} pounds.")
    print(f"{sample_kg} kilograms is {result_kg_to_oz:.2f} ounces.")