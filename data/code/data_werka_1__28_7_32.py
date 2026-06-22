def compare_and_report(num1: float, num2: float) -> bool:
    return num1 > num2

if __name__ == '__main__':
    sample_value_1 = 3.5
    sample_value_2 = 2.8
    result = compare_and_report(sample_value_1, sample_value_2)
    print(result)