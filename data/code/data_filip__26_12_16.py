def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = text[i]
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    test_cases = ["", "a", "aa", "aabbbc", "abcde"]
    for case in test_cases:
        result = run_length_encode(case)
        print(f"Input: {case!r} -> Output: {result!r}")