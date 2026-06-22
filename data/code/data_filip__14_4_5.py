def has_duplicate_chars(s: str) -> bool:
    return len(s) != len(set(s))

if __name__ == '__main__':
    sample_strings = ["hello", "world", "abcde", "aabbcc", "unique"]
    for s in sample_strings:
        result = has_duplicate_chars(s)
        print(result)