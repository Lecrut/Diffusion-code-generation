from typing import Union
def sum_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All arguments must be integers or floats.")
    return int(a + b + c)
if __name__ == '__main__':
    value1 = 10
    value2 = 5.5
    value3 = -3
    result: float | int = sum_three_variables(value1, value2, value3)
    print(f"Sum of {value1}, {value2}, and {value3} is {result}")