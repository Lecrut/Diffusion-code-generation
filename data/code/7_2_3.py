def contains_special_characters(text):
    special_characters = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
    text_set = set(text)
    return len(text_set.intersection(special_characters)) > 0

if __name__ == '__main__':
    sample_text = "Hello World"
    result = contains_special_characters(sample_text)
    print(result)