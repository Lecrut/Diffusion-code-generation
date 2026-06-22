def manipulate_case(s, case='lower'):
    valid_cases = {'lower', 'upper', 'title', 'swap'}
    if case not in valid_cases:
        raise ValueError(f'Invalid case specified: {case}. Must be one of {valid_cases}')
    if case == 'lower':
        return s.lower()
    elif case == 'upper':
        return s.upper()
    elif case == 'title':
        return s.title()
    elif case == 'swap':
        return s.swapcase()
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    print(manipulate_case(sample_string, 'lower'))
    print(manipulate_case(sample_string, 'upper'))
    print(manipulate_case(sample_string, 'title'))
    print(manipulate_case(sample_string, 'swap'))