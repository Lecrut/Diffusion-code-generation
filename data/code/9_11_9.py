def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    start = 0
    end = len(text)
    while start < end and text[start] in ' \t\n\r\x0b\x0c':
        start += 1
    while end > start and text[end - 1] in ' \t\n\r\x0b\x0c':
        end -= 1
    return text[start:end]

if __name__ == '__main__':
    sample = "   hello world   \t\n"
    print(trim_string(sample))
    sample_empty = "   "
    print(trim_string(sample_empty))
    sample_mixed = "\t\n  foo bar  \t\n"
    print(trim_string(sample_mixed))
    sample_no_whitespace = "hello"
    print(trim_string(sample_no_whitespace))
    sample_unicode_whitespace = "\u3000hello\u3000"
    print(trim_string(sample_unicode_whitespace))