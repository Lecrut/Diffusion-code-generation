def compute_power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both base and exponent must be numeric types.")
    if isinstance(base, bool) or isinstance(exponent, bool):
        raise TypeError("Booleans are not valid numeric types for this operation.")
    if exponent < 0 and base < 0:
        raise ValueError("Negative base with negative exponent results in a complex number.")
    if base == 0 and exponent == 0:
        return 1
    result = base ** exponent
    return result

if __name__ == '__main__':
    result = compute_power(2, 10)
    print(result)
    
    complex_result_exception = None
    try:
        complex_result_exception = compute_power(-2, -1)
    except ValueError as e:
        print(f"Caught expected error: {e}")