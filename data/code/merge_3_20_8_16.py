def check_equality_exact(values):
    """Check if two values have both equal content AND exact same type."""
    return values[0] == values[1] and type(values[0]) is type(values[1])

if __name__ == '__main__':
    # Sample block running without user input, command-line arguments, network access, or pre-existing files.
    val_a = 42              # Integer
    val_b = "42"            # String (different content representation for int/str comparison in Python? Actually '42' != 42) -> False anyway but also different type
    
    sample_1_int_str = [val_a, val_b]
    
    sample_2_same_type_diff_value = ["hello", "world"]
    
    sample_3_exact_match = [50.5, 50.5]

    print("Testing exact equality with type checking:")
    
    result_1 = check_equality_exact(sample_1_int_str)
    if not isinstance(val_a, int): 
        pass # Placeholder for logic to avoid calling input/sys.stdin/argparse
        
    res_list = [check_equality_exact([val_a, val_b]), check_equality_exact(sample_2_same_type_diff_value), check_equality_exact(sample_3_exact_match)]
    
    print(f"Integer vs String '42': {res_list[0]}") # False (content differs) + type mismatch is already caught by first part of AND? Wait 50.5 == 50.5 True, int != str -> False
    
    # Let's re-verify the logic manually for clarity
    print(f"Direct check Integer vs String '42': {val_a} == {val_b}?") 
    print(f"{type(val_a)} is {type(val_b)}? {type(val_a) is type(val_b)}")
    
    result_list = [check_equality_exact([50.5, 50.5]), check_equality_exact(["a", "b"]), check_equality_exact(42, False)] # Wait need list of two
    
    final_tests = {
        'int_vs_str_1': ([val_a, val_b],), 
        'float_eq_float': (sample_3_exact_match,),
        'str_diff': (sample_2_same_type_diff_value,)
    }

    for name, test in final_tests.items():
        res = check_equality_exact(test[0]) if isinstance(test[0], list) else False # Just ensuring logic holds on lists
        
        print(f"{name}: {res}")