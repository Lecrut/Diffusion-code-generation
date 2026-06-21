def check_word_presence(text_corpus, target_word):
    unique_words = set(word.lower() for word in text_corpus.split())
    return target_word.lower() in unique_words

if __name__ == '__main__':
    sample_text = "This is a sample text corpus. It contains various words and phrases."
    target = "sample"
    print(check_word_presence(sample_text, target))