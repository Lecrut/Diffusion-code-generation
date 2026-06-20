def trim_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = trim_whitespace(sample_input)
    print(result)
    assert result == "Hello World"
    print(trim_whitespace("  \t\nPython\n\t  "))
    print(trim_whitespace(""))
    print(trim_whitespace("NoWhitespace"))