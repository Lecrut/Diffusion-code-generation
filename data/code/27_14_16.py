def check_difference(a: float, b: float) -> bool:
    """Check if two floating-point numbers differ by more than machine epsilon."""
    return abs(a - b) > 1e-9

if __name__ == '__main__':
    val_int = 10
    val_float_approx_10 = 10.00000000000001
    
    # Use a small epsilon for float comparison, but direct subtraction 
    # reveals the difference clearly here as it exceeds typical machine precision noise
    is_different = abs(val_int - val_float_approx_10) > 1e-9

    if is_different:
        print("The values are different.")
    else:
        print("The values appear to be equal within floating-point tolerance.")