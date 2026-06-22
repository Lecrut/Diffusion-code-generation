def run_length_encode(input_str: str) -> str:
    if not input_str:
        return ""

    result = []
    current_char = input_str[0]
    count = 1

    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1

    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)