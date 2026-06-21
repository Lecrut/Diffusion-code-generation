def compress_rle(input_string):
    if not input_string:
        return ""

    result = []
    current_char = input_string[0]
    count = 1

    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1

    result.append(f"{count}{current_char}")

    return "".join(result)

if __name__ == '__main__':
    sample_input = "111001"
    compressed = compress_rle(sample_input)
    print(compressed)

    empty_input = ""
    compressed_empty = compress_rle(empty_input)
    print(compressed_empty)

    single_char = "1"
    compressed_single = compress_rle(single_char)
    print(compressed_single)

    complex_input = "000111000111000"
    compressed_complex = compress_rle(complex_input)
    print(compressed_complex)