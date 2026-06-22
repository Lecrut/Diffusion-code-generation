def unique_characters(phrase):
    char_map = {}
    result = []
    for char in phrase:
        if char not in char_map:
            char_map[char] = True
            result.append(char)
    return result

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_characters(sample_phrase))