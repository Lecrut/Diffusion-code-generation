def run_length_encode(data: str) -> str:
    if not data:
        return ""

    result = []
    current_char = data[0]
    count = 1

    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1

    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCDAA"
    encoded = run_length_encode(sample_input)
    print(encoded)