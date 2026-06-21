def run_length_encode(input_string):
    if not input_string:
        return ""

    if len(input_string) == 1:
        return "1" + input_string

    result = []
    current_char = input_string[0]
    count = 1

    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            if count > 3:
                result.append(str(count) + current_char)
            elif count == 3:
                result.append(current_char + current_char + current_char)
            elif count == 2:
                result.append(current_char + current_char)
            else:
                result.append(current_char)
            current_char = char
            count = 1

    if count > 3:
        result.append(str(count) + current_char)
    elif count == 3:
        result.append(current_char + current_char + current_char)
    elif count == 2:
        result.append(current_char + current_char)
    else:
        result.append(current_char)

    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaaabccc"
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)