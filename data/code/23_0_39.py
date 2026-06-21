def compare_and_report(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both values must be integers or floats.")
    
    larger = max(value1, value2)
    smaller = min(value1, value2)
    
    difference = larger - smaller
    ratio = larger / smaller if smaller != 0 else float('inf')
    
    return {
        'comparison_result': f"{larger} is greater than {smaller}",
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    result = compare_and_report(10, 5)
    print(result)