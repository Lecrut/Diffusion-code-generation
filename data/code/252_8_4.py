def compare_two_simple_quantities_now_compare(a, b):
    result = {
        'a': a,
        'b': b,
        'comparison': None
    }
    
    if a > b:
        result['comparison'] = 'greater than'
    elif a < b:
        result['comparison'] = 'less than'
    else:
        result['comparison'] = 'equal to'
    
    return result

if __name__ == '__main__':
    sample_value_1 = 75
    sample_value_2 = 30
    
    comparison_result = compare_two_simple_quantities_now_compare(sample_value_1, sample_value_2)
    print(comparison_result)