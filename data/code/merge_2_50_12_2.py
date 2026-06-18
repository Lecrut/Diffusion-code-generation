def sum_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    return a + b + c
if __name__ == '__main__':
    val1 = 10
    val2 = 5.5
    val3 = 7
    result = sum_three_variables(val1, val2, val3)
    print(result)