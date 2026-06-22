CHARACTER_THRESHOLD = 2

def extract_duplicate_characters(phrase):
    char_count = {}
    for char in phrase:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    return {char: count for char, count in char_count.items() if count > CHARACTER_THRESHOLD}

if __name__ == '__main__':
    sample_phrase = "hello world"
    duplicates = extract_duplicate_characters(sample_phrase)
    print(duplicates)