def check_negative(x):
    """Returns True if x is negative, False otherwise."""
    return x < 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input
    samples = [-5, -1.5, 0, 3]
    for val in samples:
        print(f"x={val}, is_negative={check_negative(val)}")