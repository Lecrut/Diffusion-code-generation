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
    sample = "   hello world   "
    result = trim_string(sample)
    print(result)

    sample2 = "\t\n  foo bar  \r\n"
    result2 = trim_string(sample2)
    print(result2)

    sample3 = "no_whitespace"
    result3 = trim_string(sample3)
    print(result3)

    sample4 = "   "
    result4 = trim_string(sample4)
    print(result4)

    sample5 = ""
    result5 = trim_string(sample5)
    print(result5)