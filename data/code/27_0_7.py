def check_difference(a: float, b: float) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    Optimized by using direct comparison which is efficient in Python's C implementation.
    For floating point numbers where exact equality might be problematic based on precision 
    requirements not specified here, standard operators are used as they are the most robust 
    and readable approach for general numerical difference checks without arbitrary epsilon settings.

    Args:
        a (float): First numerical value.
        b (float): Second numerical value.

    Returns:
        bool: True if a != b, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    sample_1 = 3.0
    sample_2 = 4.5
    
    result = check_difference(sample_1, sample_2)
    
    print(f"Are {sample_1} and {sample_2} different? {result}")