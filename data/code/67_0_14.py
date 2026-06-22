from typing import List

def liters_to_milliliters(liters: List[float]) -> List[float]:
    return [lit * 1000 for lit in liters]

if __name__ == '__main__':
    sample_values: List[float] = [1.5, 2.0, 0.25, 3.75]
    result: List[float] = liters_to_milliliters(sample_values)
    print(result)