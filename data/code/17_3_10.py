def rle_compress(data):
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = data[i]
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    print(rle_compress(sample_string))