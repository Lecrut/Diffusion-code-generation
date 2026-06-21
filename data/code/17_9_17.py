def run_length_encode(input_str):
    if not input_str:
        return ""

    result = []
    current_char = input_str[0]
    count = 1

    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1

    result.append(f"{current_char}{count}")

    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)

    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)

    single_char_input = "A"
    single_char_result = run_length_encode(single_char_input)
    print(single_char_result)

    complex_input = "AAAAABBBCCDEEEE"
    complex_result = run_length_encode(complex_input)
    print(complex_result)