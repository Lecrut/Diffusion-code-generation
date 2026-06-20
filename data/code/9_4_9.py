def strip_whitespace_safe(value):
    if isinstance(value, str):
        return value.strip()
    raise TypeError('Input must be a string')
if __name__ == '__main__':
    sample_inputs = ['  hello world  ', '  \t\n foo bar \t\n  ', 'no_whitespace', '', '   ', 123, None, ['list', 'input'], {'key': 'value'}]
    for sample in sample_inputs:
        try:
            result = strip_whitespace_safe(sample)
            print(f'Input: {repr(sample)} -> Output: {repr(result)}')
        except TypeError as e:
            print(f'Input: {repr(sample)} -> Error: {e}')