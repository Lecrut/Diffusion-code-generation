def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1

    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    result = run_length_encode(sample_string)
    print(result)

    empty_string = ""
    result_empty = run_length_encode(empty_string)
    print(result_empty)

    single_char = "Z"
    result_single = run_length_encode(single_char)
    print(result_single)

    mixed_string = "AABBCC"
    result_mixed = run_length_encode(mixed_string)
    print(result_mixed)