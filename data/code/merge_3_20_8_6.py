def check_equality_exact_type(value1: any, value2: any) -> bool:
    """Check if two values are equal with exact type matching."""
    return (type(value1).__name__ == 'int' and 
            type(value2).__name__ == 'int' and 
            value1 == value2) or \
           (type(value1).__name__ == 'float' and 
            type(value2).__name__ == 'float' and 
            value1 == value2) or \
           (type(value1).__name__ == 'str' and 
            type(value2).__name__ == 'str' and 
            value1 == value2)

if __name__ == '__main__':
    sample_value_1 = 42
    sample_value_2 = "hello"
    
    result = check_equality_exact_type(sample_value_1, sample_value_2)
    print(f"{sample_value_1} ({type(sample_value_1).__name__}) == {sample_value_2} ({type(sample_value_2).__name__}): {result}")