def determine_larger(value1, value2):
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return max(value1, value2)
    else:
        raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 50
    SAMPLE_VALUE_2 = 49.9
    larger_value = determine_larger(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(larger_value)