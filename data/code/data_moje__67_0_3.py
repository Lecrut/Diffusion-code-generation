from typing import List

def liters_to_milliliters(liters: List[float]) -> List[int]:
    return [int(value * 1000) for value in liters]

if __name__ == '__main__':
    sample_liters = [1.5, 0.25, 3.75]
    result = liters_to_milliliters(sample_liters)
    print(result)