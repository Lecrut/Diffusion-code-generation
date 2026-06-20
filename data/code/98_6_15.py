STR_EQUIVALENT = "apple"
STR_DIFFERENT = "banana"
NUM_LOWER_BOUND = 10
NUM_UPPER_BOUND = 15

def test_complex_scenario():
    str_a = STR_EQUIVALENT
    str_b = STR_EQUIVALENT
    str_c = STR_DIFFERENT
    num_x = NUM_LOWER_BOUND
    num_y = NUM_UPPER_BOUND
    
    condition_str_equal = (str_a == str_b)
    condition_str_unequal = (str_a != str_c)
    condition_num_lower = (num_x < num_y)
    
    if condition_str_equal and condition_str_unequal and condition_num_lower:
        return "All conditions met."
    else:
        return "One or more conditions failed."

if __name__ == '__main__':
    result = test_complex_scenario()
    print(result)