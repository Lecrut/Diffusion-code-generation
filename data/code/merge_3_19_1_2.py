def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    
    result = is_greater(sample_a, sample_b)
    
    print(f"{sample_a} > {sample_b}: {result}")