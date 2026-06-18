def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    Args:
        value (numeric): A single numerical argument
        
    Returns:
        bool: True if value equals 0, False otherwise
    """
    return value == 0

if __name__ == '__main__':
    # Sample test values run without any user input or external dependencies
    samples = [0.0, -0.5, "0", [], {}, (1,), set()]
    
    for sample in samples:
        try:
            result = is_zero(sample)
            print(f"is_zero({sample}) -> {result}")
        except TypeError as e:
            # Non-numeric types will naturally fail the comparison logic 
            # depending on Python version, but we handle gracefully here.
            # In strict numeric checks, non-numbers should return False for this task definition context
            print(f"is_zero({sample}) -> {result}")