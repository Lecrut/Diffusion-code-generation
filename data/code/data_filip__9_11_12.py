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
    sample1 = "  hello world  "
    sample2 = "\t\nLeading and trailing whitespace\r\n"
    sample3 = "no_whitespace_here"
    sample4 = ""
    sample5 = "   "

    print(repr(trim_string(sample1)))
    print(repr(trim_string(sample2)))
    print(repr(trim_string(sample3)))
    print(repr(trim_string(sample4)))
    print(repr(trim_string(sample5)))