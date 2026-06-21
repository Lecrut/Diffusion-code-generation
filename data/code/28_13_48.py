NUMBER_THRESHOLD = 0

def is_larger_than(first_number, second_number):
    return first_number > second_number

if __name__ == '__main__':
    sample_value_a = 42
    sample_value_b = 17
    result_of_comparison = is_larger_than(sample_value_a, sample_value_b)
    print(result_of_comparison)