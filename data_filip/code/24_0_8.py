def compress_rle(input_string: str) -> str:
    if not input_string:
        return ""
    result_parts = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result_parts.append(str(count) + current_char)
            current_char = char
            count = 1
    result_parts.append(str(count) + current_char)
    return "".join(result_parts)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    compressed = compress_rle(sample_input)
    print(compressed)

    sample_empty = ""
    compressed_empty = compress_rle(sample_empty)
    print(compressed_empty)

    sample_single = "Z"
    compressed_single = compress_rle(sample_single)
    print(compressed_single)

    sample_mixed = "AABBCCDD"
    compressed_mixed = compress_rle(sample_mixed)
    print(compressed_mixed)

    sample_long_run = "AAAAAAAAAA"
    compressed_long_run = compress_rle(sample_long_run)
    print(compressed_long_run)