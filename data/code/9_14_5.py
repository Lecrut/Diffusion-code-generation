def strip_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    print(strip_whitespace("  Hello World  "))
    print(strip_whitespace("   "))
    print(strip_whitespace("NoWhitespace"))
    print(strip_whitespace("\t\n Hello \t\n "))