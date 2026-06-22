def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    test_input = "aaabbccccdd"
    result = run_length_encode(test_input)
    print(result)
    test_empty = ""
    print(run_length_encode(test_empty))
    test_single = "a"
    print(run_length_encode(test_single))
    test_mixed = "aabbccddeeff"
    print(run_length_encode(test_mixed))