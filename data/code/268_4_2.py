def get_first_word(sentences):
    return [sentence.split()[0] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = ["Hello world", "Python programming", "List comprehension"]
    print(get_first_word(sample_sentences))