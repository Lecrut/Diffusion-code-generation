def detect_repeated_characters(s):
    seen = set()
    repeated = []
    seen_set = set()
    for char in s:
        if char in seen_set and char not in repeated:
            repeated.append(char)
        seen_set.add(char)
    return repeated

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "programming",
        "abcdef",
        "aabbccddeeff",
        "no repeats here",
        "repeated chars: e and a"
    ]
    for s in sample_strings:
        result = detect_repeated_characters(s)
        print(result)