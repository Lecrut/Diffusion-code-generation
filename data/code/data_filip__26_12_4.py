def run_length_encode(s: str) -> str:
    if not s:
        return ""

    if len(set(s)) == len(s):
        return s

    encoded = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1

    encoded.append(current_char + str(count))

    compressed = "".join(encoded)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCCC",
        "AAB",
        "",
        "ABC",
        "AAAAAA",
        "AABCCC"
    ]

    for sample in sample_strings:
        result = run_length_encode(sample)
        print(result)