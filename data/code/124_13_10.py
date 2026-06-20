def calculate_operations(a: float, b: float) -> tuple:
    return (a + b, a - b, a * b, a / b)

if __name__ == '__main__':
    num1 = 10.5
    num2 = 2.5
    results = calculate_operations(num1, num2)
    print(results)