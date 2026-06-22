from typing import List

def liters_to_milliliters(liters: List[float]) -> List[float]:
    return [value * 1000.0 for value in liters]

if __name__ == "__main__":
    sample_liters: List[float] = [1.5, 2.0, 0.75]
    result: List[float] = liters_to_milliliters(sample_liters)
    print(result)