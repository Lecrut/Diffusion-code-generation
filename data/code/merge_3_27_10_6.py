def check_difference(a: float, b: float) -> bool:
    """Returns True if a is different from b, False otherwise."""
    return a != b

if __name__ == '__main__':
    sample_a = 5.0
    sample_b = 10.0
    
    result = check_difference(sample_a, sample_b)
    
    print(f"check_difference({sample_a}, {sample_b}) = {result}")