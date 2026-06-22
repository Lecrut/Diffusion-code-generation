def trim_spaces(text):
    return text.strip()

if __name__ == '__main__':
    sample_text = "   Hello World   "
    print(trim_spaces(sample_text))
    print(trim_spaces("NoExtraSpaces"))
    print(trim_spaces("   \t\n  Mixed Whitespace  \t\n   "))