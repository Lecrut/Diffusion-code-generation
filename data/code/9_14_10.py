def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    sample_strings = ["  Hello World  ", "\t\nPython\t\n", "  ", "no_whitespace"]
    for s in sample_strings:
        print(strip_whitespace(s))