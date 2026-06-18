def is_larger(a: float, b: float) -> bool:
    """Returns True if a is strictly larger than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 8.2
    
    result = is_larger(sample_a, sample_b)
    
    # Print result to stdout as per standard practice for script execution without user input
    print(result)