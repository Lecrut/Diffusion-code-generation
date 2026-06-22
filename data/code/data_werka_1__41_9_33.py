def manipulate_case(s, case='lower'):
    CASE_FUNCTIONS = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title,
        'swap': str.swapcase
    }
    
    if case not in CASE_FUNCTIONS:
        raise ValueError(f"Invalid case specified: {case}. Valid cases are: {', '.join(CASE_FUNCTIONS.keys())}")
    
    return CASE_FUNCTIONS[case](s)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(manipulate_case(sample_string, 'lower'))
    print(manipulate_case(sample_string, 'upper'))
    print(manipulate_case(sample_string, 'title'))
    print(manipulate_case(sample_string, 'swap'))