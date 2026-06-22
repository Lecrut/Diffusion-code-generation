def compress_rle(input_string: str) -> str:
    if not input_string:
        return ""

    result = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1

    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCDAA"
    compressed = compress_rle(sample_input)
    print(compressed)

    sample_input_empty = ""
    compressed_empty = compress_rle(sample_input_empty)
    print(compressed_empty)

    sample_input_single = "A"
    compressed_single = compress_rle(sample_input_single)
    print(compressed_single)

    sample_input_long = "AAAAAAAAABBBBBBBBBBCCCCCCCCCDDDDDDDDD"
    compressed_long = compress_rle(sample_input_long)
    print(compressed_long)