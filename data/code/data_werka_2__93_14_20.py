def check_flags_false(flag_one, flag_two):
    is_flag_one_false = flag_one == False
    is_flag_two_false = flag_two == False
    return is_flag_one_false and is_flag_two_false

if __name__ == '__main__':
    sample_first = False
    sample_second = False
    final_result = check_flags_false(sample_first, sample_second)
    print(final_result)