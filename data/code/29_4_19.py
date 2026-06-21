def compress_text(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count == 1:
                result.append(current_char)
            else:
                result.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    if count == 1:
        result.append(current_char)
    else:
        result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaad"
    compressed_output = compress_text(sample_input)
    print(compressed_output)
    sample_input_2 = "zzzzyyxxw"
    compressed_output_2 = compress_text(sample_input_2)
    print(compressed_output_2)
    sample_input_3 = "a"
    compressed_output_3 = compress_text(sample_input_3)
    print(compressed_output_3)