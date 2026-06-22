from typing import List

def liters_to_milliliters(liters: List[float]) -> List[float]:
    return [lit * 1000 for lit in liters]

if __name__ == '__main__':
    result = liters_to_milliliters([1.5, 2.0, 0.25])
    print(result)