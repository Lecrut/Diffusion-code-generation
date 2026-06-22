def compare_and_report(value1, value2):
    result = {}
    if value1 > value2:
        larger = value1
        smaller = value2
    else:
        larger = value2
        smaller = value1
    result['difference'] = larger - smaller
    if smaller != 0:
        result['ratio'] = larger / smaller
    else:
        result['ratio'] = float('inf')
    if value1 == value2:
        result['comparison'] = 'equal'
    elif value1 > value2:
        result['comparison'] = 'value1 is greater'
    else:
        result['comparison'] = 'value2 is greater'
    return result
if __name__ == '__main__':
    sample_value1 = 42.5
    sample_value2 = 10.0
    comparison_result = compare_and_report(sample_value1, sample_value2)
    print(comparison_result)