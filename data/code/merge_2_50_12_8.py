def sum_three_numbers(a: float | int, b: float | int, c: float | int) -> float | int:
    return a + b + c
if __name__ == '__main__':
    num1 = 50
    num2 = 30.5
    num3 = 7
    result = sum_three_numbers(num1, num2, num3)
    print(result)