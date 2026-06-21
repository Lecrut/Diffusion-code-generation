def split_into_words(text):
    return text.lower().split()

if __name__ == '__main__':
    sample_text = "This is a sample sentence for word extraction and testing."
    words = split_into_words(sample_text)
    print(words)