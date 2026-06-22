def validate_exact_match(arg1, arg2):
    return arg1 == arg2

if __name__ == '__main__':
    sample_values = {
        'value1': 42,
        'value2': 42,
        'value3': 3.14,
        'value4': 3.14
    }
    
    result1 = validate_exact_match(sample_values['value1'], sample_values['value2'])
    result2 = validate_exact_match(sample_values['value3'], sample_values['value4'])
    
    print(f"Result for value1 and value2: {result1}")
    print(f"Result for value3 and value4: {result2}")