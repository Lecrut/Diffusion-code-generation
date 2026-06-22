def compare_and_report(value1, value2):
    larger = max(value1, value2)
    smaller = min(value1, value2)
    
    result = {
        'comparison': 'value1 is greater' if value1 > value2 else 'value2 is greater' if value1 < value2 else 'values are equal',
        'difference': larger - smaller,
        'ratio': larger / smaller if smaller != 0 else None
    }
    
    return result

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 24
    print(compare_and_report(sample_value1, sample_value2))