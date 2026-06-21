def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    for index in range(1, len(input_string)):
        char = input_string[index]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_input = "aaabbccccd"
    result = run_length_encode(sample_input)
    print(result)
    sample_input_two = "AaBbCc112233"
    result_two = run_length_encode(sample_input_two)
    print(result_two)
    sample_input_three = ""
    result_three = run_length_encode(sample_input_three)
    print(result_three)