def check_difference(a: float, b: float) -> bool:
    """Check if two floating-point values are different using an epsilon tolerance."""
    return abs(a - b) > 1e-9

if __name__ == '__main__':
    val_1 = 10
    val_2 = 10.00000000000001
    
    # Check if the values are different according to floating-point tolerance
    is_different = check_difference(val_1, val_2)
    
    print(f"Is {val_1} and {val_2} different? {is_different}")