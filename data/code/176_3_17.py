def extract_words(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "This is a sample sentence for word extraction and testing."
    words = extract_words(sample_text)
    print(words)