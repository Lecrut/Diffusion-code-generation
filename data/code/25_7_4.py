def compress(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1
    result.append(current_char)
    result.append(str(count))
    return "".join(result)

def check_compression(s):
    original_length = len(s)
    compressed = compress(s)
    compressed_length = len(compressed)
    return compressed_length < original_length

if __name__ == '__main__':
    sample_string = "aaabbc"
    is_compressed = check_compression(sample_string)
    print(is_compressed)