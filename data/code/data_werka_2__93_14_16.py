def check_false_pair(first_val, second_val):
    first_is_false = first_val is False
    second_is_false = second_val is False
    return first_is_false and second_is_false
if __name__ == '__main__':
    sample_one = False
    sample_two = False
    final_result = check_false_pair(sample_one, sample_two)
    print(final_result)