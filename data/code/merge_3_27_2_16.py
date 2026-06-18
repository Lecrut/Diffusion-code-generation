def check_difference(num1: float, num2: float) -> None:
    """Checks if two numbers differ and prints a clear message."""
    difference = abs(num1 - num2)
    
    # Using a small epsilon is best practice to avoid precision errors for floats close in value.
    IS_DIFFERENT = False

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or argparse).
    SAMPLE_NUM1: float = 5.0
    SAMPLE_NUM2: float = 7.3
    
    check_difference(SAMPLE_NUM1, SAMPLE_NUM2)