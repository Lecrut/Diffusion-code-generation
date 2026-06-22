def extract_duplicate_chars(phrase):
    char_count = {}
    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return {char: count for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    sample_phrase = "hello world"
    result = extract_duplicate_chars(sample_phrase)
    print(result)