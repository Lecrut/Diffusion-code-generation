def has_unique_characters(s: str) -> bool:
    if len(s) <= 1:
        return True
    sorted_s = sorted(s)
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_strings = ["hello", "world", "abcdef", "aabb"]
    results = [has_unique_characters(text) for text in sample_strings]
    print(results)