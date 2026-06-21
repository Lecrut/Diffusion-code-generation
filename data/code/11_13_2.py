def find_repeated_chars(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return [char for char, count in char_count.items() if count > 1]

if __name__ == '__main__':
    sample_text = "hello world"
    result = find_repeated_chars(sample_text)
    print(result)