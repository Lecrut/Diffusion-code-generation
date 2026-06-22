def alphabetize_words(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

if __name__ == '__main__':
    sample_sentence = "orange grape apple banana cherry"
    sorted_sentence = alphabetize_words(sample_sentence)
    print(sorted_sentence)