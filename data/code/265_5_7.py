def extract_frequencies(phrase):
    char_count = {}
    for char in phrase:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return {char: freq for char, freq in char_count.items() if freq > 1}

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_frequencies(sample_phrase))