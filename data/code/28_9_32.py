def determine_larger(value1, value2):
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return max(value1, value2)
    else:
        raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 3.14
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)