def compute_ratio(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return float(num1) / num2

if __name__ == '__main__':
    numerator = 10
    denominator = 5
    result = compute_ratio(numerator, denominator)
    print(result)