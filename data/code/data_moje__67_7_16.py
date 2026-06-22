from typing import Union

def liters_to_milliliters(value: Union[int, float]) -> Union[int, float]:
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type")
    return value * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(2))
    print(liters_to_milliliters(0.5))
    print(liters_to_milliliters(10))