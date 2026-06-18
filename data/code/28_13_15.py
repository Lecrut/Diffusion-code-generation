def determine_larger(value1: int | float, value2: int | float) -> int | float:
    """Returns the larger of two comparable numeric values."""
    return max(value1, value2)

if __name__ == '__main__':
    sample_int_1 = 45
    sample_float_1 = 3.7
    result1 = determine_larger(sample_int_1, sample_float_1)
    print(result1)