from typing import Union

def liter_to_milliliter(value: Union[int, float]) -> Union[int, float]:
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type (int or float).")
    if isinstance(value, bool):
        raise TypeError("Input must be a numeric type (int or float).")
    return value * 1000

if __name__ == '__main__':
    sample_value = 2.5
    result = liter_to_milliliter(sample_value)
    print(result)
    
    sample_integer = 10
    result_int = liter_to_milliliter(sample_integer)
    print(result_int)