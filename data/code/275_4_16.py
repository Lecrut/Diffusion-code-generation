def are_chars_unique(char_set):
    seen = set()
    for char in char_set:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample_chars = "abcdefg"
    print(are_chars_unique(sample_chars))