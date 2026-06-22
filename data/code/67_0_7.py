from typing import List

def convert_to_milliliters(liters: List[float]) -> List[float]:
    return [lit * 1000 for lit in liters]

if __name__ == '__main__':
    sample_liters = [1.5, 2.0, 0.5]
    result = convert_to_milliliters(sample_liters)
    print(result)