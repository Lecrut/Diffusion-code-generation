def determine_larger(value1, value2):
    type_map = {
        (int, int): lambda x, y: max(x, y),
        (float, float): lambda x, y: max(x, y),
        (int, float): lambda x, y: max(float(x), y),
        (float, int): lambda x, y: max(x, float(y))
    }
    
    value_types = (type(value1), type(value2))
    if value_types in type_map:
        return type_map[value_types](value1, value2)
    else:
        raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    sample_value1 = 25.7
    sample_value2 = 40
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)