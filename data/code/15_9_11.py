def compress_string(input_str: str) -> str:
    if not input_str:
        return ""

    compressed: list[str] = []
    count: int = 1
    current_char: str = input_str[0]

    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = input_str[i]
            count = 1

    compressed.append(current_char)
    compressed.append(str(count))

    compressed_str: str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(input_str) else input_str

if __name__ == '__main__':
    sample_input: str = "aabcccccaaa"
    result: str = compress_string(sample_input)
    print(result)