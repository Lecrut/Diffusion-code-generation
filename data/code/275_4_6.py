def are_characters_unique(characters):
    seen = set()
    for char in characters:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    print(are_characters_unique(sample_string))