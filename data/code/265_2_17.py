def extract_non_repeated_chars(phrase):
    char_count = {}
    non_repeated_chars = []

    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in phrase:
        if char_count[char] == 1 and char not in non_repeated_chars:
            non_repeated_chars.append(char)

    return ''.join(non_repeated_chars)

if __name__ == '__main__':
    sample_phrase = "Hello World! 123"
    result = extract_non_repeated_chars(sample_phrase)
    print(result)