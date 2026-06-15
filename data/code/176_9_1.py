def extract_words(text):
    return text.split()
if __name__ == '__main__':
    sample_string = "This is a sample sentence for word extraction"
    word_list = extract_words(sample_string)
    print(word_list)