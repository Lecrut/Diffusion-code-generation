def compare_and_report(value1, value2):
    result = {}
    
    if value1 > value2:
        larger = value1
        smaller = value2
    else:
        larger = value2
        smaller = value1
    
    result['comparison'] = 'value1' if value1 > value2 else 'value2'
    result['difference'] = abs(value1 - value2)
    
    if smaller != 0:
        result['ratio'] = larger / smaller
    else:
        result['ratio'] = float('inf')
    
    return result

if __name__ == '__main__':
    sample_value1 = 42.5
    sample_value2 = 18.3
    print(compare_and_report(sample_value1, sample_value2))