def compress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    length = len(data)
    i = 1
    while i < length:
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1
        i += 1
    result.append(current_char)
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccd"
    print(compress_rle(sample_input))