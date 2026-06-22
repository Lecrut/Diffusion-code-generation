def manipulate_case(text, case='lower'):
    CASE_FUNCTIONS = {'lower': str.lower, 'upper': str.upper, 'title': str.title, 'swap': str.swapcase}
    if case not in CASE_FUNCTIONS:
        raise ValueError(f"Invalid case specified: {case}. Valid cases are: {('', ', '.join(CASE_FUNCTIONS.keys()))}")
    return CASE_FUNCTIONS[case](text)
if __name__ == '__main__':
    sample_text = 'Hello World Example'
    try:
        print(manipulate_case(sample_text, 'lower'))
        print(manipulate_case(sample_text, 'upper'))
        print(manipulate_case(sample_text, 'title'))
        print(manipulate_case(sample_text, 'swap'))
        print(manipulate_case(sample_text, 'invalid'))
    except ValueError as e:
        print(e)