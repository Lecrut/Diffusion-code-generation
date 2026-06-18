def check_difference():
    """Check if 10 and a slightly larger float are different."""
    val_a = 10
    val_b = 10.00000000000001
    
    # Use the != operator for direct value comparison
    is_different = val_a != val_b
    
    return is_different

if __name__ == '__main__':
    result = check_difference()
    
    if result:
        print("The values are different.")
    else:
        print("The values appear to be the same (within float precision limits).")