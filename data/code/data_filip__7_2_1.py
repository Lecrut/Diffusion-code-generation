def contains_special_characters(text):
    special_symbols = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
    text_chars = set(text)
    return bool(text_chars.intersection(special_symbols))

if __name__ == '__main__':
    sample_string = "Hello World!123"
    result = contains_special_characters(sample_string)
    print(result)