def check_string_length(input_string):
    is_long = len(input_string) > 10
    return is_long
if __name__ == '__main__':
    sample_string_one = "short"
    sample_string_two = "this_is_a_long_string"
    sample_string_three = "tenchars"
    result_one = check_string_length(sample_string_one)
    print(f"'{sample_string_one}' is long: {result_one}")
    result_two = check_string_length(sample_string_two)
    print(f"'{sample_string_two}' is long: {result_two}")
    result_three = check_string_length(sample_string_three)
    print(f"'{sample_string_three}' is long: {result_three}")