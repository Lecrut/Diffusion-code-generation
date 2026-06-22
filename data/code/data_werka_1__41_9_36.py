def manipulate_case(s, case='lower'):
    valid_cases = {'lower', 'upper', 'title', 'swap'}
    if case not in valid_cases:
        raise ValueError(f'Invalid case specified: {case}. Valid cases are: {valid_cases}')
    
    case_functions = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title,
        'swap': str.swapcase
    }
    
    return case_functions[case](s)

if __name__ == '__main__':
    sample_text_1 = "Python Programming"
    print(manipulate_case(sample_text_1, 'lower'))
    print(manipulate_case(sample_text_1, 'upper'))
    print(manipulate_case(sample_text_1, 'title'))
    print(manipulate_case(sample_text_1, 'swap'))

    sample_text_2 = "OpenAI ChatGPT"
    print(manipulate_case(sample_text_2, 'lower'))
    print(manipulate_case(sample_text_2, 'upper'))
    print(manipulate_case(sample_text_2, 'title'))
    print(manipulate_case(sample_text_2, 'swap'))