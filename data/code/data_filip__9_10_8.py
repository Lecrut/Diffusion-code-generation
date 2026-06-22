def strip_whitespace(text):
    return text.strip()
if __name__ == '__main__':
    sample_values = ['   hello world   ', '\t\n  python  \r\n', 'no_extra_spaces', '  leading_only', 'trailing_only  ', '   both_ends   ', '', '   ']
    for value in sample_values:
        result = strip_whitespace(value)
        print(f'Input: {repr(value)} -> Output: {repr(result)}')