def encode_segments(text):
    if not text:
        return
    length = len(text)
    start = 0
    while start < length:
        end = start + 1
        while end < length and text[end] == text[start]:
            end += 1
        yield (text[start], end - start)
        start = end

if __name__ == '__main__':
    result = list(encode_segments("aaabbc"))
    print(result)