def perform_arithmetic(a: int, b: float) -> dict:
    results = {
        'addition': a + int(b),
        'subtraction': a - int(b),
        'multiplication': a * int(b)
    }
    if b != 0:
        results['division'] = a / b
    else:
        results['division'] = "Error: Division by zero"
    return results

if __name__ == '__main__':
    num1 = 10
    num2 = 5.5
    output = perform_arithmetic(num1, num2)
    print(output)