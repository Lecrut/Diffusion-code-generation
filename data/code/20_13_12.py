def compare_values(val1, val2):
    """
    Compares two values to determine if they are equal.
    
    Args:
        val1 (any): The first value to compare.
        val2 (any): The second value to compare.
        
    Returns:
        bool: True if the values are equal, False otherwise.
    """
    try:
        return val1 == val2
    except TypeError as e:
        print(f"Error: Cannot compare these types ({type(val1).__name__} and {type(val2).__name__}).")
        raise

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input.
    sample_val_1 = 42
    sample_val_2 = "42"
    
    print("Comparing hard-coded sample values:")
    result = compare_values(sample_val_1, sample_val_2)
    if result:
        print(f"{sample_val_1} is equal to {sample_val_2}")
    else:
        print(f"{sample_val_1} is not equal to {sample_val_2}")

    # Additional test case with same types and values.
    sample_val_3 = 42
    sample_val_4 = 42
    
    result_same = compare_values(sample_val_3, sample_val_4)
    if result_same:
        print(f"{sample_val_3} is equal to {sample_val_4}")
    else:
        print(f"{sample_val_3} is not equal to {sample_val_4}")

    # Test case with incompatible types (int vs float that look similar).
    sample_val_5 = 10.0
    sample_val_6 = "10"
    
    result_float_str = compare_values(sample_val_5, sample_val_6)
    if result_float_str:
        print(f"{sample_val_5} is equal to {sample_val_6}")
    else:
        print(f"{sample_val_5} is not equal to {sample_val_6}")

    # Test case with incompatible types (int vs string).
    sample_val_7 = 10
    sample_val_8 = "hello"
    
    result_int_str = compare_values(sample_val_7, sample_val_8)
    if result_int_str:
        print(f"{sample_val_7} is equal to {sample_val_8}")
    else:
        print(f"{sample_val_7} is not equal to {sample_val_8}")