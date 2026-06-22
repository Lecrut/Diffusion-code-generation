def compress_rle(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAAA"
    compressed_output = compress_rle(sample_string)
    print(compressed_output)