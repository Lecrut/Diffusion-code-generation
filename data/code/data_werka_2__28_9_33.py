def determine_larger(value1, value2):
    comparison_map = {
        (int, int): lambda x, y: max(x, y),
        (float, float): lambda x, y: max(x, y),
        (int, float): lambda x, y: max(float(x), y),
        (float, int): lambda x, y: max(x, float(y))
    }
    
    key = (type(value1), type(value2))
    if key in comparison_map:
        return comparison_map[key](value1, value2)
    else:
        raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    sample_value1 = 7.5
    sample_value2 = 42
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)