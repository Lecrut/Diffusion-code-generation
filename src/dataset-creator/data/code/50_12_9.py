def sum_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    for value in [a, b, c]:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            continue
        else:
            raise TypeError(f"Invalid argument '{value}'. Expected int or float.")
    result = 0
    is_float = False
    for value in [a, b, c]:
        if isinstance(value, float) or (isinstance(value, int) and not isinstance(value, bool)):
            pass
    return a + b + c
if __name__ == '__main__':
    val1: float | int = 10.5
    val2: float | int = 20
    val3: float | int = -5
    total_sum = sum_three_variables(val1, val2, val3)
    print(f"Sum of {val1}, {val2}, and {val3} is: {total_sum}")