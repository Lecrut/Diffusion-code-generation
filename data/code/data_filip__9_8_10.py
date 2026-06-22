def strip_whitespace(s): return s.strip()

if __name__ == '__main__':
    print(strip_whitespace("  Hello World  "))
    print(strip_whitespace("\t\nPython\n\t"))
    print(strip_whitespace("NoSpaces"))