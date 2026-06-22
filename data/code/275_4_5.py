def are_characters_unique(characters):
    char_count = {}
    for char in characters:
        if char in char_count:
            return False
        char_count[char] = 1
    return True
if __name__ == '__main__':
    sample_chars = 'abcdefg'
    result = are_characters_unique(sample_chars)
    print(result)
    sample_chars_with_duplicates = 'hello'
    result = are_characters_unique(sample_chars_with_duplicates)
    print(result)