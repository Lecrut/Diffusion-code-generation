def run_length_encode(s: str) -> str:
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    test_strings = ["", "a", "aa", "aabbbcccc", "a1b2c3"]
    for s in test_strings:
        print(run_length_encode(s))