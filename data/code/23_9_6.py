def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded_chars = []
    current_char = input_string[0]
    count = 1
    length = len(input_string)
    index = 1

    while index < length:
        char = input_string[index]
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(current_char)
            if count > 1:
                encoded_chars.append(str(count))
            current_char = char
            count = 1
        index += 1

    encoded_chars.append(current_char)
    if count > 1:
        encoded_chars.append(str(count))

    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_input = "aabbbccdddd"
    result = run_length_encode(sample_input)
    print(result)