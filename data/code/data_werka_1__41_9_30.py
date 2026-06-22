def manipulate_case(s, case='lower'):
    valid_cases = {'lower': str.lower, 'upper': str.upper, 'title': str.title, 'swap': str.swapcase}
    if case not in valid_cases:
        raise ValueError(f"Invalid case specified: {case}. Choose from 'lower', 'upper', 'title', or 'swap'.")
    return valid_cases[case](s)
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    print(manipulate_case(sample_string, 'lower'))
    print(manipulate_case(sample_string, 'upper'))
    print(manipulate_case(sample_string, 'title'))
    print(manipulate_case(sample_string, 'swap'))