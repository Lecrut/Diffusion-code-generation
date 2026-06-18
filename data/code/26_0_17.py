def is_greater(a: any, b: any) -> bool:
    """Returns True if a is strictly greater than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    
    result_1 = is_greater(sample_a, sample_b)
    
    print(f"Testing: {sample_a} vs {sample_b}")
    if not (is_greater(3.5, 2) or isinstance(result_1, bool)):
        raise ValueError("Function logic verification failed.")
        
    assert result_1 == True