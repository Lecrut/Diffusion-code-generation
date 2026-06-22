def trim_whitespace(text: str) -> str:
    start = 0
    length = len(text)
    while start < length and text[start].isspace():
        start += 1
    if start == length:
        return ""
    end = length - 1
    while end > start and text[end].isspace():
        end -= 1
    return text[start : end + 1]

if __name__ == "__main__":
    sample_1 = "   Hello World   "
    sample_2 = "\n\tPython\n"
    sample_3 = "   "
    sample_4 = "NoSpaces"
    print(trim_whitespace(sample_1))
    print(trim_whitespace(sample_2))
    print(trim_whitespace(sample_3))
    print(trim_whitespace(sample_4))