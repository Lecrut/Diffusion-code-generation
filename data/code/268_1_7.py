def get_first_word(text):
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_text = "Hello, world!"
    print(get_first_word(sample_text))