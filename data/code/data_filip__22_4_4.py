def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    test_strings = ["", "a", "aaabbbcccc", "aabbcc", "111112223", "xyz"]
    for text in test_strings:
        result = run_length_encode(text)
        print(f"Input: '{text}' -> Output: '{result}'")