def run_length_encode(binary_string: str) -> str:
    if not binary_string:
        return ""

    encoded_parts = []
    current_char = binary_string[0]
    count = 1

    for char in binary_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded_parts.append(f"{count}{current_char}")

    return "".join(encoded_parts)

if __name__ == '__main__':
    print(run_length_encode("1100100111"))
    print(run_length_encode("1"))
    print(run_length_encode(""))