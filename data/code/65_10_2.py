import sys

def feet_to_inches(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError("feet must be a number")
    if feet < 0:
        raise ValueError("feet cannot be negative")
    return feet * 12

if __name__ == '__main__':
    sample_value = 5.5
    result = feet_to_inches(sample_value)
    print(result)