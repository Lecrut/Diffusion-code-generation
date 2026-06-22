def strip_whitespace(s): return s.strip()
if __name__ == '__main__':
    print(strip_whitespace("  hello world  "))
    print(strip_whitespace("\t\n  test  \r\n"))
    print(strip_whitespace("no_spaces"))