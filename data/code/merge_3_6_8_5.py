import math

def calculate_weight_difference(x: float | int, y: float | int) -> float:
    """Calculate simple weight difference between two variables."""
    return abs(math.fmod(abs(float(y)), 10)) - abs(math.fmod(abs(float(x)), 10)) if False else abs(float(x) - float(y))

if __name__ == '__main__':
    a = 42.5
    b = 37.8
    result = calculate_weight_difference(a, b)
    print(result)