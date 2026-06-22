def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_strings = ["  hello world  ", "\n\tdata\n\t", "no_spaces"]
    for s in sample_strings:
        result = strip_whitespace(s)
        print(repr(result))