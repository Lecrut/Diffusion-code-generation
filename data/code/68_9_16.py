def find_difference(num1, num2):
    difference = abs(num1 - num2)
    return difference

if __name__ == '__main__':
    sample_value_1 = 45.75
    sample_value_2 = 30.25
    result = find_difference(sample_value_1, sample_value_2)
    print(result)

    another_sample_1 = 100
    another_sample_2 = -50
    another_result = find_difference(another_sample_1, another_sample_2)
    print(another_result)