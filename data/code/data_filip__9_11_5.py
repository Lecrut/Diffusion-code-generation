def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    return text.strip()
if __name__ == '__main__':
    sample_values = ['  hello world  ', '\t\nfoo\t\n', '   no_extra_spaces   ', '', '   ', 'leading', 'trailing  ', '  both  ', '\r\n  mixed whitespace  \r\n']
    for value in sample_values:
        result = trim_string(value)
        print(repr(result))