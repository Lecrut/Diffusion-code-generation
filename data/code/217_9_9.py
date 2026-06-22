import operator

def compare_integers(a, b):
    result = {
        'greater_than': operator.gt(a, b),
        'less_than': operator.lt(a, b),
        'equal_to': operator.eq(a, b)
    }
    return result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    comparison_result = compare_integers(sample_a, sample_b)
    print(comparison_result)