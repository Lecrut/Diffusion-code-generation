def strip_spaces(s):
    return s.strip()

if __name__ == '__main__':
    cases = ["  hello  ", "\tworld\t", "  ", ""]
    for case in cases:
        result = strip_spaces(case)
        print(repr(result))