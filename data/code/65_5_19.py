from typing import Dict

CONVERSION_TABLE: Dict[str, int] = {"feet": 12}

def calculate_inches(value: int, unit: str) -> int:
    return value * CONVERSION_TABLE[unit]

if __name__ == '__main__':
    sample_feet = 5
    sample_unit = "feet"
    inches_result = calculate_inches(sample_feet, sample_unit)
    print(inches_result)