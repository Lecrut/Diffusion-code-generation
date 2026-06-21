def compress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = data[i]
            count = 1
    result.append(current_char)
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAABBB"
    compressed_output = compress_rle(sample_string)
    print(compressed_output)