from typing import Union

def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    input_value: float = 2.5
    result: float = liters_to_milliliters(input_value)
    print(result)