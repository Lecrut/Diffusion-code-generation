def are_characters_unique(char_set):
    unique_chars = set()
    for char in char_set:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True

if __name__ == '__main__':
    sample_chars = "abcdefg"
    print(are_characters_unique(sample_chars))