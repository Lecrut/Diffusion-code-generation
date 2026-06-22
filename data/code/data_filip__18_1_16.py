def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded_chars = []
    char_count = 1
    current_char = input_string[0]

    for i in range(1, len(input_string)):
        next_char = input_string[i]
        if next_char == current_char:
            char_count += 1
        else:
            encoded_chars.append(current_char)
            if char_count > 1:
                encoded_chars.append(str(char_count))
            current_char = next_char
            char_count = 1

    encoded_chars.append(current_char)
    if char_count > 1:
        encoded_chars.append(str(char_count))

    return "".join(encoded_chars)

if __name__ == '__main__':
    input_data = "AAAABBBCCDAA"
    result = run_length_encode(input_data)
    print(result)