def extract_duplicate_characters(phrase):
    char_count = {}
    for char in phrase:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    return {char: count for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    sample_phrase = "Hello world! This is a test sentence, with punctuation."
    duplicates = extract_duplicate_characters(sample_phrase)
    print(duplicates)