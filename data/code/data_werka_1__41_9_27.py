def manipulate_case(s, case='lower'):
    valid_cases = {'lower', 'upper', 'title', 'swap'}
    if case not in valid_cases:
        raise ValueError(f"Invalid case specified: {case}. Valid cases are: {valid_cases}")
    
    operations = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title,
        'swap': str.swapcase
    }
    
    return operations[case](s)

if __name__ == '__main__':
    sample_string = "Python Programming"
    print(manipulate_case(sample_string, 'lower'))
    print(manipulate_case(sample_string, 'upper'))
    print(manipulate_case(sample_string, 'title'))
    print(manipulate_case(sample_string, 'swap'))