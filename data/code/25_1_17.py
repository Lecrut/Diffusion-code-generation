def is_zero(value):
    """Returns True if value is zero (or 0j), False otherwise."""
    return value == 0

if __name__ == '__main__':
    # Sample values to test without user input or command line arguments
    samples = [0, -0.1, 3e-40, float('inf'), complex(0, 0)]
    
    for s in samples:
        print(f"Input: {s}, is_zero: {is_zero(s)}")