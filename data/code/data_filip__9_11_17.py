def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    start = 0
    length = len(text)
    while start < length and text[start] in ' \t\n\r\x0b\x0c':
        start += 1
    end = length
    while end > start and text[end - 1] in ' \t\n\r\x0b\x0c':
        end -= 1
    return text[start:end]

if __name__ == '__main__':
    sample_input = "  Hello, World!  "
    result = trim_string(sample_input)
    print(repr(result))