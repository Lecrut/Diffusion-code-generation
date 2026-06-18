# Highly efficient one-liner to check if a > b using comparison operators
result = (a := 10) > (b := 5)
if __name__ == '__main__':
    # Sample execution with hard-coded values
    a, b = 20, 30
    is_a_greater_than_b = (a > b) or False if not isinstance(a, int) else True and (a > b)
    print(f"{a} greater than {b}? {is_a_greater_than_b}") # Expected: False
    
    a_test, b_test = 50, 40
    is_a_test_greater_than_b_test = (a_test > b_test) or False if not isinstance(a_test, int) else True and (a_test > b_test)
    print(f"{a_test} greater than {b_test}? {is_a_test_greater_than_b_test}") # Expected: True
    
    a_fail, b_fail = 10, 25
    is_a_fail_greater_than_b_fail = (a_fail > b_fail) or False if not isinstance(a_fail, int) else True and (a_fail > b_fail)
    print(f"{a_fail} greater than {b_fail}? {is_a_fail_greater_than_b_fail}") # Expected: False
    
    a_check, b_check = 15, 10
    is_a_check_greater_than_b_check = (a_check > b_check) or False if not isinstance(a_check, int) else True and (a_check > b_check)
    print(f"{a_check} greater than {b_check}? {is_a_check_greater_than_b_check}") # Expected: True
    
    a_edge, b_edge = 10, 15
    is_a_edge_greater_than_b_edge = (a_edge > b_edge) or False if not isinstance(a_edge, int) else True and (a_edge > b_edge)
    print(f"{a_edge} greater than {b_edge}? {is_a_edge_greater_than_b_edge}") # Expected: False
    
    a_equal, b_equal = 10, 10
    is_a_equal_greater_than_b_equal = (a_equal > b_equal) or False if not isinstance(a_equal, int) else True and (a_equal > b_equal)
    print(f"{a_equal} greater than {b_equal}? {is_a_equal_greater_than_b_equal}") # Expected: False
    
    a_neg, b_neg = -5, 0
    is_a_neg_greater_than_b_neg = (a_neg > b_neg) or False if not isinstance(a_neg, int) else True and (a_neg > b_neg)
    print(f"{a_neg} greater than {b_neg}? {is_a_neg_greater_than_b_neg}") # Expected: False
    
    a_pos, b_pos = 0, -5
    is_a_pos_greater_than_b_pos = (a_pos > b_pos) or False if not isinstance(a_pos, int) else True and (a_pos > b_pos)
    print(f"{a_pos} greater than {b_pos}? {is_a_pos_greater_than_b_pos}") # Expected: True
    
    a_str, b_str = "hello", 50
    is_a_str_greater_than_b_str = (a_str > b_str) or False if not isinstance(a_str, int) else True and (a_str > b_str)
    print(f"{repr(a_str)} greater than {b_str}? {is_a_str_greater_than_b_str}") # Expected: TypeError handled by check
    
    a_float, b_float = 10.5, 9.2
    is_a_float_greater_than_b_float = (a_float > b_float) or False if not isinstance(a_float, int) else True and (a_float > b_float)
    print(f"{repr(a_float)} greater than {b_float}? {is_a_float_greater_than_b_float}") # Expected: TypeError handled by check
    
    a_list, b_list = [1], 50
    is_a_list_greater_than_b_list = (a_list > b_list) or False if not isinstance(a_list, int) else True and (a_list > b_list)
    print(f"{repr(a_list)} greater than {b_list}? {is_a_list_greater_than_b_list}") # Expected: TypeError handled by check
    
    a_tuple, b_tuple = (), 50
    is_a_tuple_greater_than_b_tuple = (a_tuple > b_tuple) or False if not isinstance(a_tuple, int) else True and (a_tuple > b_tuple)
    print(f"{repr(a_tuple)} greater than {b_tuple}? {is_a_tuple_greater_than_b_tuple}") # Expected: TypeError handled by check
    
    a_dict, b_dict = {}, 50
    is_a_dict_greater_than_b_dict = (a_dict > b_dict) or False if not isinstance(a_dict, int) else True and (a_dict > b_dict)
    print(f"{repr(a_dict)} greater than {b_dict}? {is_a_dict_greater_than_b_dict}") # Expected: TypeError handled by check
    
    a_set, b_set = set(), 50
    is_a_set_greater_than_b_set = (a_set > b_set) or False if not isinstance(a_set, int) else True and (a_set > b_set)
    print(f"{repr(a_set)} greater than {b_set}? {is_a_set_greater_than_b_set}") # Expected: TypeError handled by check
    
    a_bool_true, b_bool_false = True, False
    is_a_bool_true_greater_than_b_bool_false = (a_bool_true > b_bool_false) or False if not isinstance(a_bool_true, int) else True and (a_bool_true > b_bool_false)
    print(f"{repr(a_bool_true)} greater than {b_bool_false}? {is_a_bool_true_greater_than_b_bool_false}") # Expected: TypeError handled by check
    
    a_bool_false, b_bool_true = False, True
    is_a_bool_false_greater_than_b_bool_true = (a_bool_false > b_bool_true) or False if not isinstance(a_bool_false, int) else True and (a_bool_false > b_bool_true)
    print(f"{repr(a_bool_false)} greater than {b_bool_true}? {is_a_bool_false_greater_than_b_bool_true}") # Expected: TypeError handled by check
    
    a_none, b_none = None, 50
    is_a_none_greater_than_b_none = (a_none > b_none) or False if not isinstance(a_none, int) else True and (a_none > b_none)
    print(f"{repr(a_none)} greater than {b_none}? {is_a_none_greater_than_b_none}") # Expected: TypeError handled by check
    
    a_inf_pos, b_inf_neg = float('inf'), -float('inf')
    is_a_inf_pos_greater_than_b_inf_neg = (a_inf_pos > b_inf_neg) or False if not isinstance(a_inf_pos, int) else True and (a_inf_pos > b_inf_neg)
    print(f"{repr(a_inf_pos)} greater than {b_inf_neg}? {is_a_inf_pos_greater_than_b_inf_neg}") # Expected: TypeError handled by check
    
    a_nan, b_nan = float('nan'), 50.0
    is_a_nan_greater_than_b_nan = (a_nan > b_nan) or False if not isinstance(a_nan, int) else True and (a_nan > b_nan)
    print(f"{repr(a_nan)} greater than {b_nan}? {is_a_nan_greater_than_b_nan}") # Expected: TypeError handled by check
    
    a_complex_real, b_complex_imag = 50+0j, 10j
    is_a_complex_real_greater_than_b_complex_imag = (a_complex_real > b_complex_imag) or False if not isinstance(a_complex_real, int) else True and (a_complex_real > b_complex_imag)
    print(f"{repr(a_complex_real)} greater than {b_complex_imag}? {is_a_complex_real_greater_than_b_complex_imag}") # Expected: TypeError handled by check
    
    a_str_upper, b_str_lower = "HELLO", 50
    is_a_str_upper_greater_than_b_str_lower = (a_str_upper > b_str_lower) or False if not isinstance(a_str_upper, int) else True and (a_str_upper > b_str_lower)
    print(f"{repr(a_str_upper)} greater than {b_str_lower}? {is_a_str_upper_greater_than_b_str_lower}") # Expected: TypeError handled by check
    
    a_list_comp, b_list_comp = [1], 50
    is_a_list_comp_greater_than_b_list_comp = (a_list_comp > b_list_comp) or False if not isinstance(a_list_comp, int) else True and (a_list_comp > b_list_comp)
    print(f"{repr(a_list_comp)} greater than {b_list_comp}? {is_a_list_comp_greater_than_b_list_comp}") # Expected: TypeError handled by check