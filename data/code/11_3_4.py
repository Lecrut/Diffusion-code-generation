def get_repeated_char_frequencies(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    return repeated_chars

if __name__ == '__main__':
    sample_string = "hello world"
    result = get_repeated_char_frequencies(sample_string)
    print(result)