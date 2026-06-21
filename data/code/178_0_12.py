def split_into_words(text):
    return [word for word in text.strip().split() if word]

if __name__ == '__main__':
    sample_text = "  Hello   world! This is a test.  "
    print(split_into_words(sample_text))