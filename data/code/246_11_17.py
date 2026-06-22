def sum_with_precision(a: float, b: float) -> float:
    return a + b

if __name__ == '__main__':
    num1 = 123.4567890123456789
    num2 = 987.6543210987654321
    result = sum_with_precision(num1, num2)
    print(result)