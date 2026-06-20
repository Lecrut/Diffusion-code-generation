def trim_string(text: str) -> str:
    start = 0
    length = len(text)
    while start < length and text[start].isspace():
        start += 1
    end = length
    while end > start and text[end - 1].isspace():
        end -= 1
    return text[start:end]

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = trim_string(sample_input)
    print(result)