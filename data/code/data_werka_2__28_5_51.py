def compare_and_report(num1: float, num2: float) -> bool:
    is_greater = num1 > num2
    return is_greater

if __name__ == '__main__':
    sample_value1 = 7.2
    sample_value2 = 5.8
    result = compare_and_report(sample_value1, sample_value2)
    print(f"Is {sample_value1} strictly greater than {sample_value2}?", result)