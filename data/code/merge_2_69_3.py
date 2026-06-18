import math
def grams_to_pounds(grams: float) -> float:
    if not isinstance(grams, (int, float)):
        raise TypeError("Input must be a number.")
    if grams < 0:
        raise ValueError("Mass cannot be negative.")
    return grams * 0.00220462
def kilograms_to_ounces(kg: float) -> float:
    if not isinstance(kg, (int, float)):
        raise TypeError("Input must be a number.")
    if kg < 0:
        raise ValueError("Mass cannot be negative.")
    return kg * 35.274
def pounds_to_kilograms(pounds: float) -> float:
    if not isinstance(pounds, (int, float)):
        raise TypeError("Input must be a number.")
    if pounds < 0:
        raise ValueError("Mass cannot be negative.")
    return pounds * 0.453592
def ounces_to_grams(ounces: float) -> float:
    if not isinstance(ounces, (int, float)):
        raise TypeError("Input must be a number.")
    if ounces < 0:
        raise ValueError("Mass cannot be negative.")
    return ounces * 28.3495
def convert_mass(unit1: str, value1: float, unit2: str) -> float:
    valid_units = ['grams', 'pounds', 'kilograms', 'ounces']
    if unit1 not in valid_units or unit2 not in valid_units:
        raise ValueError(f"Invalid units. Must be one of {valid_units}")
    if value1 < 0:
        raise ValueError("Mass cannot be negative.")
    gram_value = 0
    if unit1 == 'grams':
        gram_value = value1
    elif unit1 == 'pounds':
        gram_value = pounds_to_kilograms(value1) * 1000 / grams_to_pounds(1)                                                         
        pass
    if unit1 == 'grams':
        gram_value = value1
    elif unit1 == 'pounds':
        gram_value = grams_to_pounds(0) * (value1 / 0.45359237)                                                        
        gram_value = value1 * 453.59237
    elif unit1 == 'kilograms':
        gram_value = value1 * 1000
    elif unit1 == 'ounces':
        gram_value = value1 * 28.3495
    if unit2 == 'grams':
        return gram_value
    elif unit2 == 'pounds':
        return gram_value / 453.59237
    elif unit2 == 'kilograms':
        return gram_value / 1000
    elif unit2 == 'ounces':
        return gram_value / 28.3495
if __name__ == '__main__':
    print(f"{grams_to_pounds(500):.6f} pounds")
    print(f"{kilograms_to_ounces(10):.6f} ounces")
    print(f"{pounds_to_kilograms(2):.6f} kilograms")
    print(f"{ounces_to_grams(8):.6f} grams")
    result = convert_mass('kilograms', 5, 'ounces')
    print(f"5 kg to ounces: {result:.6f}")