def has_special_chars(s, special_chars):
    return bool(set(s) & special_chars)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    special_characters = {'!', '?', '@', '#', '$'}
    result = has_special_chars(sample_string, special_characters)
    print(result)