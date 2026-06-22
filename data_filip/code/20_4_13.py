def run_length_encode(input_str):
    if not input_str:
        return ""

    encoded_list = []
    current_char = input_str[0]
    count = 1

    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_list.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded_list.append(f"{count}{current_char}")

    return "".join(encoded_list)

if __name__ == '__main__':
    text = "AAAABBBCCDAA"
    result = run_length_encode(text)
    print(result)