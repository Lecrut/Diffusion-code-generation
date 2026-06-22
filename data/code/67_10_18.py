from typing import Union

def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    sample_liters: float = 2.5
    result: float = liters_to_milliliters(sample_liters)
    print(result)