def calculate_difference(num1: float, num2: float) -> float:
    return round(num1 - num2, 4)

if __name__ == '__main__':
    sample_num1 = 15.789
    sample_num2 = 7.654
    result = calculate_difference(sample_num1, sample_num2)
    print(result)