def sum_three_numbers(a: float | int, b: float | int, c: float | int) -> float | int:
    for value in [a, b, c]:
        if not isinstance(value, (int, float)):
            raise TypeError(f"All arguments must be numbers. Got {type(value).__name__} instead.")
    return a + b + c
if __name__ == '__main__':
    num1: int = 42
    num2: float = 3.5
    num3: int = -7
    total_sum = sum_three_numbers(num1, num2, num3)
    print(f"Sum of {num1}, {num2}, and {num3} is: {total_sum}")