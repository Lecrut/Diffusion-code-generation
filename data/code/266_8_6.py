def count_words(text):
    return len(list(filter(None, text.lower().split())))

if __name__ == '__main__':
    sample_text = "Hello World! This is a test."
    print(count_words(sample_text))