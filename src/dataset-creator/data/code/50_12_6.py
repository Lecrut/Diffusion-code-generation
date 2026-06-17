def sum_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    return a + b + c
if __name__ == '__main__':
    val1 = 5
    val2 = 3.7
    val3 = 4
    total_sum = sum_three_variables(val1, val2, val3)
    print(total_sum)