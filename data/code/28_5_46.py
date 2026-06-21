def compare_and_report(num1: float, num2: float) -> bool:
    STRICT_INEQUALITY_THRESHOLD = 0.0
    return num1 - num2 > STRICT_INEQUALITY_THRESHOLD

if __name__ == '__main__':
    result = compare_and_report(7.2, 5.9)
    print(result)