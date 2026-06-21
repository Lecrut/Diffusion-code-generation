def compress_sequence(s: str) -> str:
    if not s:
        return ""
    
    if len(s) == 0:
        return ""

    result = []
    prev_char = s[0]
    count = 1
    length = len(s)
    index = 1

    while index < length:
        current_char = s[index]
        if current_char == prev_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
                result.append(prev_char)
            else:
                result.append(prev_char)
            prev_char = current_char
            count = 1
        index += 1

    if count > 1:
        result.append(str(count))
        result.append(prev_char)
    else:
        result.append(prev_char)

    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccc"
    compressed_output = compress_sequence(sample_input)
    print(compressed_output)