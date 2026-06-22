def compare_and_report(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both values must be integers or floats.")
    
    result = {}
    if value1 > value2:
        larger = value1
        smaller = value2
    else:
        larger = value2
        smaller = value1
    
    result['comparison'] = 'value1 is greater' if value1 > value2 else 'value2 is greater' if value2 > value1 else 'both are equal'
    result['difference'] = abs(value1 - value2)
    result['ratio'] = larger / smaller if smaller != 0 else float('inf')
    
    return result

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 7.5
    print(compare_and_report(sample_value1, sample_value2))