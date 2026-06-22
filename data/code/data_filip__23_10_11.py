def run_length_encode(s):
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1

    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_strings = [
        "AAABBC",
        "XYZ",
        "A",
        "",
        "AAaaBB",
        "111222333"
    ]

    for s in sample_strings:
        encoded = run_length_encode(s)
        print(encoded)