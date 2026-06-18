def sum_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All arguments must be integers or floats.")
    result = a + b + c
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        return result                                                   
    else:
        return float(result)
if __name__ == '__main__':
    val1 = 5
    val2 = 3.7
    val3 = 4
    total_sum = sum_three_variables(val1, val2, val3)
    print(f"Sum of {val1}, {val2}, and {val3} is: {total_sum}")