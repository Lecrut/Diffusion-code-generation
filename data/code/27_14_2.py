def check_difference():
    """Check if 10 and a slightly larger float differ using direct comparison."""
    val_a = 10
    val_b = 10.00000000000001
    
    # Direct equality/inequality works for floats in Python as it uses IEEE 754 representation.
    # Unlike integers, floating-point numbers can have tiny differences due to precision limits.
    is_different = val_a != val_b

if __name__ == '__main__':
    if check_difference():
        print("The values are different.")
    else:
        print("The values are the same.")