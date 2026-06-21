def compress_string(input_str: str) -> str:
    if not input_str:
        return ""

    compressed = []
    current_char = input_str[0]
    count = 1

    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = char
            count = 1

    compressed.append(current_char + str(count))

    compressed_str = "".join(compressed)

    if len(compressed_str) < len(input_str):
        return compressed_str
    else:
        return input_str

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)