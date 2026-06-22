def are_characters_unique(characters):
    seen = set()
    for char in characters:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample_chars = "abcdefg"
    print("Unique:", are_characters_unique(sample_chars))

    sample_chars_with_duplicates = "abcdeffg"
    print("Unique:", are_characters_unique(sample_chars_with_duplicates))