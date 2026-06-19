def are_values_different(a, b):
    return abs(a - b) > 1e-10

if __name__ == '__main__':
    sample_values = {
        'value1': 10,
        'value2': 10.00000000000001
    }
    
    result = are_values_different(sample_values['value1'], sample_values['value2'])
    print(result)