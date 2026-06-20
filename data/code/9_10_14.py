def strip_whitespace(text):
    return text.strip()
if __name__ == '__main__':
    sample_strings = ['  hello world  ', '\t\n  leading and trailing whitespace  \n\t', 'no leading or trailing', '   only leading', 'only trailing   ', '', '   ']
    for s in sample_strings:
        result = strip_whitespace(s)
        print(f'Original: {repr(s)} -> Stripped: {repr(result)}')