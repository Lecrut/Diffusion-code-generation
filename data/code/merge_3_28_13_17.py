def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """Returns the larger of two comparable numeric values."""
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    
    return value1 if value1 > value2 else value2

if __name__ == '__main__':
    # Sample test cases with hardcoded values
    sample_ints = determine_larger(30, 50)
    sample_floats = determine_larger(-4.7, -2.9)
    sample_mixed = determine_larger(100, 99.9)

    print(f"Larger of {30} and {50}: {sample_ints}")
    print(f"Larger of {-4.7} and {-2.9}: {sample_floats}")
    print(f"Larger of {100} and {99.9}: {sample_mixed}")