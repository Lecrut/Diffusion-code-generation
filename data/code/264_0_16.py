def find_words(text):
    words = text.split()
    return words

if __name__ == '__main__':
    sample_text = "This is an example of a sentence with multiple words."
    print(find_words(sample_text))