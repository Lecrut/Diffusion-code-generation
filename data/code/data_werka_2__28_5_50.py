def compare_and_report(num1: float, num2: float) -> bool:
    STRICT_INEQUALITY_THRESHOLD = 0.00001
    if abs(num1 - num2) < STRICT_INEQUALITY_THRESHOLD:
        return False
    return num1 > num2

if __name__ == '__main__':
    result = compare_and_report(7.5, 6.99998)
    print(result)