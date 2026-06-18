def check_different():
    """Check if 10 is different from a value very slightly larger than itself."""
    val1 = 10
    val2 = 10.00000000000001
    
    # Use != operator to compare inequality directly in Python's idiom style.
    return val1 != val2

if __name__ == '__main__':
    result = check_different()
    if result:
        print("The values are different.")
    else:
        print("The values are the same.")