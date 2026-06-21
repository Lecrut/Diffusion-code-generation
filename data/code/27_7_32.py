def compare_inequality(a, b):
    return a != b

if __name__ == '__main__':
    sample_values = {
        'value1': 42,
        'value2': 3.14
    }
    
    result = compare_inequality(sample_values['value1'], sample_values['value2'])
    print(result)