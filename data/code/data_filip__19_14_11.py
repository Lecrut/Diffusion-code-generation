def rle_compress(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = data[i]
            count = 1
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCDDEEE"
    compressed = rle_compress(sample_string)
    print(compressed)