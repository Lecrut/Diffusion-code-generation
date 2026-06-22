def run_length_encode(s):
    if not s:
        return {}
    counts = {}
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if current_char in counts:
                counts[current_char] += count
            else:
                counts[current_char] = count
            current_char = s[i]
            count = 1
    if current_char in counts:
        counts[current_char] += count
    else:
        counts[current_char] = count
    return counts

if __name__ == '__main__':
    test_strings = [
        "aaabbc",
        "11112233333",
        "",
        "abcdef",
        "aabbccddaabbcc"
    ]
    for text in test_strings:
        result = run_length_encode(text)
        print(f"Input: '{text}' -> Output: {result}")