def count_words(text):
    return len(text.split())

if __name__ == '__main__':
    sample_text = "Hello World! This is a test."
    print(count_words(sample_text.lower()))