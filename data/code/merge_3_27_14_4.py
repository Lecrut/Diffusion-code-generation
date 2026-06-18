def check_difference(a: float, b: float) -> bool:
    """Check if two floating-point numbers are different using a small epsilon."""
    return abs(a - b) > 1e-9

if __name__ == '__main__':
    val1 = 10.0
    val2 = 10.0 + 1e-15
    
    if check_difference(val1, val2):
        print("The values are different.")
    else:
        print("The values appear to be equal due to floating-point precision limits.")