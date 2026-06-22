def trim_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    print(trim_whitespace("  hello world  "))
    print(trim_whitespace("\t\nfoo\t\n"))
    print(trim_whitespace("  "))
    print(trim_whitespace(""))
    print(trim_whitespace("no spaces"))