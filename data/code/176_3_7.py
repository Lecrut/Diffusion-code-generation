def split_sentence(text):
    words = text.split()
    return words

if __name__ == '__main__':
    sample_text = "This is a sample sentence for word extraction and testing."
    result = split_sentence(sample_text)
    print(result)