def check_difference(a: float, b: float) -> bool:
    """Returns True if a is different from b, False otherwise."""
    return not (a == b)

if __name__ == '__main__':
    # Sample test cases running without external input or files
    sample_a = 10.5
    sample_b = 20.3
    
    result = check_difference(sample_a, sample_b)
    
    print(f"check_difference({sample_a}, {sample_b}) returned: {result}")