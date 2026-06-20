def sum_and_diff(a: int, b: int) -> (int, int):
    return a + b, a - b

if __name__ == '__main__':
    num1 = 20
    num2 = 8
    result = sum_and_diff(num1, num2)
    print(result)