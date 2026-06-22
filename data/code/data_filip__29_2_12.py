def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    for index in range(1, len(input_string)):
        if input_string[index] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = input_string[index]
            count = 1
    encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    result = run_length_encode(sample_string)
    print(result)
    empty_result = run_length_encode("")
    print(empty_result)
    single_result = run_length_encode("z")
    print(single_result)