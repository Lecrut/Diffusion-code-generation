def compare_values(value1: float, value2: float) -> bool:
    return value1 > value2

if __name__ == '__main__':
    sample_values = {
        'sample_value1': 3.14,
        'sample_value2': 2.71
    }
    
    result = compare_values(sample_values['sample_value1'], sample_values['sample_value2'])
    print(result)