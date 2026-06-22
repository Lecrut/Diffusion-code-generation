def run_length_encode(digits: str) -> str:
    if not digits:
        return ""
    result = []
    current_char = digits[0]
    count = 1
    for char in digits[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    input_sequence = "1122233334"
    encoded = run_length_encode(input_sequence)
    print(encoded)