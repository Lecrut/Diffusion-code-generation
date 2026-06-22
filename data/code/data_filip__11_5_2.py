def detect_repeated_characters(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen and char not in repeated:
            repeated.append(char)
        seen.add(char)
    return repeated

if __name__ == '__main__':
    sample_strings = [
        "programming",
        "hello",
        "abcabc",
        "abcdef",
        "aabbccdd",
        ""
    ]
    for sample in sample_strings:
        result = detect_repeated_characters(sample)
        print(f"Input: '{sample}' -> Repeated characters: {result}")