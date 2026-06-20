def has_special_characters(s, special_chars):
    return len(set(s) & special_chars) > 0

if __name__ == '__main__':
    sample_string = "Hello, World!"
    predefined_special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/'}
    result = has_special_characters(sample_string, predefined_special_chars)
    print(result)