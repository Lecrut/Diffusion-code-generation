def has_unique_chars_sorted(s):
    if not s:
        return True
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "hello",
        "world!",
        "unique",
        "aabbcc",
        "",
        "a"
    ]
    for sample in sample_strings:
        result = has_unique_chars_sorted(sample)
        print(f"{sample!r}: {result}")