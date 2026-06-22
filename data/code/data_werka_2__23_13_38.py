def compare_values(value1, value2):
    comparison_map = {
        'greater': "First value is greater than the second value.",
        'less': "First value is less than the second value.",
        'equal': "First value is equal to the second value."
    }
    
    if value1 > value2:
        return comparison_map['greater']
    elif value1 < value2:
        return comparison_map['less']
    else:
        return comparison_map['equal']

if __name__ == '__main__':
    sample_value1 = 50
    sample_value2 = 30
    result = compare_values(sample_value1, sample_value2)
    print(result)