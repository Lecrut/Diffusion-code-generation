def trim_string(text: str) -> str:
    if not text:
        return text
    start = 0
    end = len(text)
    while start < end and text[start] in '\t\n\r\x0b\x0c ' :
        start += 1
    while end > start and text[end - 1] in '\t\n\r\x0b\x0c ':
        end -= 1
    return text[start:end]

if __name__ == '__main__':
    sample_values = [
        "   hello world   ",
        "\t\n foo \r\n",
        "no_trim",
        "   ",
        "",
        "  leading and trailing  ",
        "\x0b\x0c middle \x0b\x0c"
    ]
    for sample in sample_values:
        result = trim_string(sample)
        print(repr(result))