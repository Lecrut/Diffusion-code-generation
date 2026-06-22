def is_all_unique(characters):
    seen = set()
    for char in characters:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample_chars = "abcdefg"
    result = is_all_unique(sample_chars)
    print(result)