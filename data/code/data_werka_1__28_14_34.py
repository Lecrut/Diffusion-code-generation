def compare_values(value1, value2):
    if not isinstance(value1, float) or not isinstance(value2, float):
        raise ValueError("Both inputs must be of type float.")
    
    return value1 > value2

if __name__ == '__main__':
    sample_value1 = 3.14
    sample_value2 = 2.71
    result = compare_values(sample_value1, sample_value2)
    print(result)