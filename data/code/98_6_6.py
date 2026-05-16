import sys
def run_complex_test():
    str_a = "apple"
    str_b = "apple"
    str_c = "banana"
    num_x = 10
    num_y = 15
    num_z = 10
    condition_str_equal = (str_a == str_b)
    condition_str_unequal = (str_a != str_c)
    condition_num_greater = (num_x > num_y)
    condition_num_less = (num_z < num_y)
    all_conditions_met = condition_str_equal and condition_str_unequal and condition_num_greater and condition_num_less
    if all_conditions_met:
        print("All complex conditions are simultaneously true.")
if __name__ == '__main__':
    run_complex_test()