import sys
def test_complex_scenario():
    str_a = "apple"
    str_b = "apple"
    str_c = "banana"
    num_x = 10
    num_y = 12
    condition_str_equal = (str_a == str_b)
    condition_str_unequal = (str_a != str_c)
    condition_num_greater = (num_x > num_y)
    condition_num_less = (num_x < num_y)
    all_conditions_met = condition_str_equal and condition_str_unequal and condition_num_greater
    if all_conditions_met:
        print("Scenario met: String equality and string inequality and numerical inequality are all true.")
if __name__ == '__main__':
    test_complex_scenario()