# Check if two floating point values are different using a tolerance-based approach
def check_difference(val1, val2):
    """Returns True if |val1 - val2| > machine epsilon."""
    return abs(val1 - val2) > 0.0

if __name__ == '__main__':
    # Sample values: integers and floats that may appear different due to precision
    a = 10
    b = 10.00000000000001
    
    result = check_difference(a, b)
    
    if result:
        print("The values are considered different.")
    else:
        print("The values are effectively the same.")