def compare_and_report(num1: float, num2: float) -> bool:
    return num1 < num2

if __name__ == '__main__':
    sample_num1 = 3.5
    sample_num2 = 4.2
    result = compare_and_report(sample_num1, sample_num2)
    print(result)