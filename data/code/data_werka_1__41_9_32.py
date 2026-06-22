def manipulate_case(s: str, case: str='lower') -> str:
    cases = {'lower': s.lower(), 'upper': s.upper(), 'title': s.title(), 'swap': s.swapcase()}
    return cases.get(case, s)
if __name__ == '__main__':
    sample_string = 'Hello World'
    print(manipulate_case(sample_string))
    print(manipulate_case(sample_string, 'upper'))
    print(manipulate_case(sample_string, 'title'))
    print(manipulate_case(sample_string, 'swap'))
    print(manipulate_case(sample_string, 'invalid'))