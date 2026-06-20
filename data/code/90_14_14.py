def is_greater_than_ten(num1, num2):
    return num1 > 10 or num2 > 10

if __name__ == '__main__':
    sample_num1 = 8
    sample_num2 = 15
    result = is_greater_than_ten(sample_num1, sample_num2)
    print(result)