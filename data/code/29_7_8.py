def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("111222333"))