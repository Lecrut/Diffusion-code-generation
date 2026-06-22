def compare_and_report(value1, value2):
    larger = max(value1, value2)
    smaller = min(value1, value2)
    
    result = {
        'comparison': f"{larger} is greater than {smaller}" if larger != smaller else "Both values are equal",
        'difference': larger - smaller,
        'ratio': larger / smaller if smaller != 0 else 'undefined'
    }
    
    return result

if __name__ == '__main__':
    value1 = 42
    value2 = 7
    print(compare_and_report(value1, value2))