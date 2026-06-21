def compare_and_report(num1: float, num2: float) -> bool:
    if num1 <= num2:
        return False
    return True

if __name__ == '__main__':
    result = compare_and_report(7.0, 5.2)
    print(result)