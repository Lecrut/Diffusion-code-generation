from typing import Tuple, Dict

CONSTANTS: Dict[str, float] = {
    "base": 12.5,
    "height": 7.2,
    "multiplier": 0.5
}

def compute_area(dimensions: Dict[str, float]) -> float:
    return dimensions["multiplier"] * dimensions["base"] * dimensions["height"]

if __name__ == "__main__":
    area_result = compute_area(CONSTANTS)
    print(area_result)