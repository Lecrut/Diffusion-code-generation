def rle_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    length = len(text)
    for i in range(1, length):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(str(count) + text[i - 1])
            count = 1
    result.append(str(count) + text[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'AABBCC'
    encoded_output = rle_encode(sample_input)
    print(encoded_output)