def count_words(text):
    return len(text.split())

if __name__ == '__main__':
    sample_text = "This is a sample sentence with seven words."
    word_count = count_words(sample_text)
    print(word_count)