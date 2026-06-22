def manipulate_case(s: str, case: str='lower') -> str:
    if case == 'lower':
        return s.lower()
    elif case == 'upper':
        return s.upper()
    elif case == 'title':
        return s.title()
    elif case == 'swap':
        return s.swapcase()
    else:
        raise ValueError(f'Unsupported case: {case}')
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    print(manipulate_case(sample_string))
    print(manipulate_case(sample_string, 'upper'))
    print(manipulate_case(sample_string, 'title'))
    print(manipulate_case(sample_string, 'swap'))
    try:
        print(manipulate_case(sample_string, 'invalid'))
    except ValueError as e:
        print(e)