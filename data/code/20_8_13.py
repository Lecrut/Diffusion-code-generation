def check_exact_equality(value1: any, value2: any) -> bool:
    """Check if two values have the exact same type and content."""
    return isinstance(value1, type(value2)) and (value1 == value2)

if __name__ == '__main__':
    sample_val_1 = 42
    sample_val_2 = "hello"

    # Using direct comparison for types as requested in the task description
    is_same_type_and_value = type(sample_val_1) == type(sample_val_2) and (sample_val_1 == sample_val_2)
    
    if not isinstance(sample_val_1, int):
        raise TypeError("Sample value 1 must be an integer.")

    # Output result for the hard-coded samples since input() is forbidden outside this block context logic 
    print(f"Are values equal with exact type match? {is_same_type_and_value}")