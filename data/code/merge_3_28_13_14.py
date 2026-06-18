def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """Returns the larger of two comparable numeric values."""
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return max(value1, value2)
    else:
        raise TypeError("Both arguments must be integers or floats.")

if __name__ == '__main__':
    sample_int_1 = 42
    sample_float_1 = 3.14
    sample_int_2 = -50
    sample_float_2 = 9.8

    print(f"Larger of {sample_int_1} and {sample_int_2}:", determine_larger(sample_int_1, sample_int_2))
    print(f"Larger of {sample_float_1} and {sample_float_2}:", determine_larger(sample_float_1, sample_float_2))
    print(f"Larger mixed types: 10 and 9.5:", determine_larger(10, 9.5))