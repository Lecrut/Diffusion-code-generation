def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    print(strip_whitespace("  hello  "))
    print(strip_whitespace("\t\nworld\t\n"))
    print(strip_whitespace("no whitespace"))
    print(strip_whitespace(""))
    print(strip_whitespace("   "))