def compress_string(data):
    if not data:
        return ""
    compressed = []
    count = 1
    length = len(data)
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(f"{data[i - 1]}{count}")
            count = 1
    compressed.append(f"{data[length - 1]}{count}")
    result = "".join(compressed)
    if len(result) >= len(data):
        return data
    return result

if __name__ == '__main__':
    sample_input = "aaabbbccccd"
    print(compress_string(sample_input))
    sample_empty = ""
    print(compress_string(sample_empty))
    sample_single = "a"
    print(compress_string(sample_single))
    sample_no_compress = "abcdefg"
    print(compress_string(sample_no_compress))