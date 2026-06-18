def is_larger(a: float | int, b: float | int) -> bool:
    """Returns True if a is strictly larger than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 7.2
    
    result = is_larger(sample_a, sample_b)
    
    print(f"is_larger({sample_a}, {sample_b}) = {result}")