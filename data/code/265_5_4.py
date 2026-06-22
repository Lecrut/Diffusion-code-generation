def extract_duplicate_chars(phrase):
    char_count = {}
    for char in phrase:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return {char: count for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(extract_duplicate_chars(sample_phrase))