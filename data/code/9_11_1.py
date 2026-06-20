def trim_string(text: str) -> str:
    if not text:
        return text
    start = 0
    end = len(text)
    while start < end and text[start] in ' \t\n\r\x0b\x0c':
        start += 1
    while end > start and text[end - 1] in ' \t\n\r\x0b\x0c':
        end -= 1
    return text[start:end]

if __name__ == '__main__':
    sample1 = '  hello world  '
    print(trim_string(sample1))
    sample2 = '\t\n  spaced  \n\t'
    print(trim_string(sample2))
    sample3 = ''
    print(trim_string(sample3))
    sample4 = 'nochange'
    print(trim_string(sample4))
    sample5 = '   '
    print(trim_string(sample5))