def compress_string(text):
    if not text:
        return ""
    groups = []
    current_group = [text[0]]
    for i in range(1, len(text)):
        char = text[i]
        prev_char = text[i - 1]
        if char == prev_char:
            current_group.append(char)
        else:
            groups.append("".join(current_group))
            current_group = [char]
    groups.append("".join(current_group))
    compressed_parts = []
    for group in groups:
        char_val = group[0]
        num_val = len(group)
        compressed_parts.append(f"{char_val}{num_val}")
    return "".join(compressed_parts)

if __name__ == '__main__':
    input_data = "xxxyyyzz"
    output_data = compress_string(input_data)
    print(output_data)