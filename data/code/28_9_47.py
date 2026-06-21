def determine_larger(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both values must be integers or floats")
    
    def compare_numbers(a, b):
        return a if a > b else b
    
    return compare_numbers(value1, value2)

if __name__ == '__main__':
    sample_value1 = 25
    sample_value2 = 78.9
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)