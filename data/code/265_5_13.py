def extract_duplicate_characters(phrase):
    char_count = {}
    for char in phrase:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    result = extract_duplicate_characters(sample_phrase)
    print(result)