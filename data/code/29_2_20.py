def run_length_encode(s: str) -> str:
    if not s:
        return ""

    encoded = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1

    encoded.append(str(count) + current_char)

    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    result = run_length_encode(sample_text)
    print(result)