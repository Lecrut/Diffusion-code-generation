def count_words(text):
    return len(text.split())

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(count_words(sample_text))