from typing import Union
def grams_to_pounds(grams: float) -> str:
    if not isinstance(grams, (int, float)) or grams < 0:
        raise ValueError("Input must be a non-negative number.")
    return f"{grams} grams = {round(grams / 453.592, 6)} pounds"
def kilograms_to_ounces(kg: Union[int, float]) -> str:
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Input must be a non-negative number.")
    return f"{kg} kilograms = {round(kg * 35.274, 6)} ounces"
def pounds_to_kilograms(pounds: Union[int, float]) -> str:
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Input must be a non-negative number.")
    return f"{pounds} pounds = {round(pounds * 0.453592, 6)} kilograms"
def ounces_to_grams(ounces: Union[int, float]) -> str:
    if not isinstance(ounces, (int, float)) or ounces < 0:
        raise ValueError("Input must be a non-negative number.")
    return f"{ounces} ounces = {round(ounces * 28.3495, 6)} grams"
if __name__ == '__main__':
    print(grams_to_pounds(100))
    print(kilograms_to_ounces(2))
    print(pounds_to_kilograms(5))
    print(ounces_to_grams(8))