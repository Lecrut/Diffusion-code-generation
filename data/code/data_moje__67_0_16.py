from typing import List, Dict, Union

UNIT_CONVERSIONS: Dict[str, float] = {"liter_to_milliliter": 1000.0}

def liters_to_milliliters(liters: List[Union[int, float]]) -> List[float]:
    factor: float = UNIT_CONVERSIONS["liter_to_milliliter"]
    return [value * factor for value in liters]

if __name__ == '__main__':
    test_data: List[Union[int, float]] = [1.25, 0, 3.5, 100]
    print(liters_to_milliliters(test_data))