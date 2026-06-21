def compress_rle(input_string):
    if not input_string:
        return ''

    compressed_parts = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1

    compressed_parts.append(f"{count}{current_char}")
    return ''.join(compressed_parts)

if __name__ == '__main__':
    sample_input = "AAABBBCCDAA"
    result = compress_rle(sample_input)
    print(result)