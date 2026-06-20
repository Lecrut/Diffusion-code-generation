def capitalize_first_char(strings: list[str]) -> list[str]:
    return [s[:1].upper() + s[1:] if s else s for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "", "python", "test"]
    result = capitalize_first_char(sample_strings)
    print(result)