def trim_string(input_text: str) -> str:
    return ''.join(input_text.split(' ')).replace('  ', ' ').strip()
if __name__ == '__main__':
    sample_input: str = "   hello   world   "
    cleaned: str = trim_string(sample_input)
    print(cleaned)
    sample_two: str = "\t\n  test  \r\n"
    print(trim_string(sample_two))