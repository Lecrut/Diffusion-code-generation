def compress_text(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(text[i - 1])
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(text[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    compressed_output = compress_text(sample_input)
    print(compressed_output)