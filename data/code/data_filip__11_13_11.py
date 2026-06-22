def find_repeated_characters(text):
    all_chars = set(text)
    unique_chars = set()
    repeated_chars_set = set()
    for char in text:
        if char in unique_chars:
            repeated_chars_set.add(char)
        else:
            unique_chars.add(char)
    return sorted(list(repeated_chars_set))
if __name__ == '__main__':
    sample_text = 'programming'
    result = find_repeated_characters(sample_text)
    print(result)