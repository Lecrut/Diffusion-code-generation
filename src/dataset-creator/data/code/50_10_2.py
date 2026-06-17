from typing import Union
def calculate_sum(a: float, b: float, c: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All arguments must be numeric.")
    return a + b + c
if __name__ == '__main__':
    val1 = 10.5
    val2 = 20
    val3 = -5.7
    try:
        result = calculate_sum(val1, val2, val3)
        print(f"The sum is {result}")
    except TypeError as e:
        print(f"Error: {e}")