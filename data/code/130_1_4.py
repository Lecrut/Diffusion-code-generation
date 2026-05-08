def check_zero_sample(number):
    if number == 0:
        return "The number is zero."
    else:
        return "The number is not zero."
if __name__ == '__main__':
    sample_value_1 = 0
    result_1 = check_zero_sample(sample_value_1)
    print(result_1)
    sample_value_2 = 42
    result_2 = check_zero_sample(sample_value_2)
    print(result_2)
    sample_value_3 = -5
    result_3 = check_zero_sample(sample_value_3)
    print(result_3)