def has_special_intersection(text, special_chars):
    return bool(set(text) & special_chars)

if __name__ == '__main__':
    special_characters = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")
    sample_text = "Hello World!"
    result = has_special_intersection(sample_text, special_characters)
    print(result)