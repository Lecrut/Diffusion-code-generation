from typing import Union
def calculate_sum(a: float, b: float, c: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All arguments must be numeric.")
    return a + b + c
if __name__ == '__main__':
    value_a = 10.5
    value_b = 20
    value_c = -3.7
    total_sum = calculate_sum(value_a, value_b, value_c)
    print(total_sum)