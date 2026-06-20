def contains_special_chars(text):
    special_symbols = set("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")
    return bool(set(text) & special_symbols)

if __name__ == '__main__':
    sample_string = "Hello World!"
    result = contains_special_chars(sample_string)
    print(result)