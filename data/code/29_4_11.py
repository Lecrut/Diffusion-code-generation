def compress_text(text):
    if not text:
        return ""
    result = []
    count = 1
    length = len(text)
    for i in range(1, length):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(text[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    result.append(text[length - 1])
    if count > 1:
        result.append(str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccddeeef"
    compressed_output = compress_text(sample_input)
    print(compressed_output)