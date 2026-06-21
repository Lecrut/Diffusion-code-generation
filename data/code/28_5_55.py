def compare_and_report(num1: float, num2: float) -> bool:
    is_greater = (num1 > num2)
    return is_greater

if __name__ == '__main__':
    sample_num1 = 7.2
    sample_num2 = 5.9
    result = compare_and_report(sample_num1, sample_num2)
    print(f"Is {sample_num1} strictly greater than {sample_num2}? {result}")