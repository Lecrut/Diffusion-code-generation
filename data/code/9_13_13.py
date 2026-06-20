def trim_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    print(trim_whitespace("  hello world  "))
    print(trim_whitespace("\t\n spaced out \n\t"))
    print(trim_whitespace("already_trimmed"))
    print(trim_whitespace("   "))
    print(trim_whitespace(""))