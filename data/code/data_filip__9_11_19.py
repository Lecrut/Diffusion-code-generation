def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    left = 0
    right = len(text) - 1
    while left <= right and text[left].isspace():
        left += 1
    while right >= left and text[right].isspace():
        right -= 1
    if left > right:
        return ""
    return text[left:right + 1]

if __name__ == '__main__':
    samples = [
        "  hello world  ",
        "\t\n  spaced out  \n\t",
        "   ",
        "",
        "no spaces",
        "\t\n",
        "   leading only",
        "trailing only   ",
        "  both  ends  ",
        "\t\n\r\x0b\x0c mixed whitespace \x0c\x0b\r\n\t"
    ]
    for sample in samples:
        result = trim_string(sample)
        print(repr(sample), "->", repr(result))