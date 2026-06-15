def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    sample_string = "This is a sample sentence for testing word counting."
    word_count = count_words(sample_string)
    print(word_count)