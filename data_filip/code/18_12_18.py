def run_length_encode(text: str) -> str:
    if not text:
        return ""

    encoded = []
    count = 1
    current_char = text[0]

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    print(run_length_encode("AAAABBBCCDAA"))
    print(run_length_encode("A"))
    print(run_length_encode(""))
    print(run_length_encode("ABC"))
    print(run_length_encode("AAAAA"))