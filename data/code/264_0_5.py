def find_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(find_words(sample_text))