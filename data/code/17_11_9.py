def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""

    encoded_parts = []
    current_char = input_string[0]
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = input_string[i]
            count = 1

    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = run_length_encode(sample_input)
    print(result)

    sample_input_empty = ""
    result_empty = run_length_encode(sample_input_empty)
    print(result_empty)

    sample_input_single = "x"
    result_single = run_length_encode(sample_input_single)
    print(result_single)

    sample_input_no_repeats = "abcdef"
    result_no_repeats = run_length_encode(sample_input_no_repeats)
    print(result_no_repeats)

    sample_input_all_same = "aaaaa"
    result_all_same = run_length_encode(sample_input_all_same)
    print(result_all_same)