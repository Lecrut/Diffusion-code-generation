def trim_spaces(text):
    return text.strip()
if __name__ == '__main__':
    sample_strings = ['   hello world   ', '  python  ', '   ', 'no_extra_spaces', '   leading_only', 'trailing_only   ', '', '   multiple   spaces   inside   ']
    for s in sample_strings:
        result = trim_spaces(s)
        print(repr(result))