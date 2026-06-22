MAX_PRECISION = 10 ** (-10)

def precise_addition(a: float, b: float) -> float:
    while abs(a + b - (a - MAX_PRECISION)) > MAX_PRECISION:
        a += MAX_PRECISION
    return a + b
if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    result = precise_addition(num1, num2)
    print(result)