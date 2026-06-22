def extract_duplicate_chars(phrase):
    char_count = {}
    for char in phrase:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return {char: count for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    print(extract_duplicate_chars("Hello World!"))