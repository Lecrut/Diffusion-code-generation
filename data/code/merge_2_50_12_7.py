def sum_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All arguments must be integers or floats.")
    return a + b + c
if __name__ == '__main__':
    val1: int = 5
    val2: float = 3.7
    val3: int = -2
    total_sum = sum_three_variables(val1, val2, val3)
    print(f"Sum of {val1}, {val2}, and {val3} is: {total_sum}")