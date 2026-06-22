def are_characters_unique(char_set):
    seen_chars = set()
    for char in char_set:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

if __name__ == '__main__':
    sample_chars = "abcdefg"
    result = are_characters_unique(sample_chars)
    print(result)