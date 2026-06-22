def compare_and_report(value1, value2):
    result = {}
    
    if value1 > value2:
        larger = value1
        smaller = value2
    else:
        larger = value2
        smaller = value1
    
    result['comparison'] = 'value1 is greater' if value1 > value2 else 'value2 is greater' if value2 > value1 else 'both values are equal'
    result['difference'] = larger - smaller
    result['ratio'] = larger / smaller if smaller != 0 else float('inf')
    
    return result

if __name__ == '__main__':
    sample_value1 = 42.5
    sample_value2 = 10.3
    print(compare_and_report(sample_value1, sample_value2))