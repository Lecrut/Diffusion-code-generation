def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = s[i]
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

def is_compression_effective(s):
    if not s:
        return False
    encoded = run_length_encode(s)
    return len(encoded) < len(s)

if __name__ == '__main__':
    test_cases = [
        "AAAABBBCCDAA",
        "AAAAAAAAAA",
        "A",
        "ABCDE",
        "aaabbbccc"
    ]
    for text in test_cases:
        encoded_version = run_length_encode(text)
        original_length = len(text)
        encoded_length = len(encoded_version)
        effective = is_compression_effective(text)
        print(f"Original: '{text}' (len={original_length}) -> Encoded: '{encoded_version}' (len={encoded_length}), Effective: {effective}")