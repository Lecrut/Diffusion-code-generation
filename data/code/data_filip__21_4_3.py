def run_length_encode(s):
    if not s:
        return {}
    result = {}
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

def run_length_decode(encoded_dict):
    result = []
    for char, count in encoded_dict.items():
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCDAA",
        "ABC",
        "AABBCC",
        "AAAAAAAAAA",
        ""
    ]
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded!r}")
        print()