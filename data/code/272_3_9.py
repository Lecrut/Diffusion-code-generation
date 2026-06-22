def alphabetize_words(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

if __name__ == '__main__':
    sample_sentence = "orange grape apple mango banana cherry"
    result = alphabetize_words(sample_sentence)
    print(result)