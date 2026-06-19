def manipulate_case(s, case='lower'):
    VALID_CASES = {'lower', 'upper', 'title', 'swap'}
    
    if case not in VALID_CASES:
        raise ValueError(f'Invalid case specified: {case}. Valid cases are: {VALID_CASES}')
    
    CASE_FUNCTIONS = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title,
        'swap': str.swapcase
    }
    
    return CASE_FUNCTIONS[case](s)

if __name__ == '__main__':
    SAMPLE_TEXT = "Hello, World!"
    print(manipulate_case(SAMPLE_TEXT, 'lower'))
    print(manipulate_case(SAMPLE_TEXT, 'upper'))
    print(manipulate_case(SAMPLE_TEXT, 'title'))
    print(manipulate_case(SAMPLE_TEXT, 'swap'))