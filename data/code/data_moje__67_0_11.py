from typing import List

def convert_liters_to_milliliters(liters: List[float]) -> List[float]:
    return [value * 1000 for value in liters]

if __name__ == '__main__':
    sample_values: List[float] = [1.5, 2.0, 0.75, 3.25]
    print(convert_liters_to_milliliters(sample_values))