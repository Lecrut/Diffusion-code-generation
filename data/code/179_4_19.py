def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError('Input must be a string')
    words = [word.strip() for word in sentence.split(' ') if word.strip()]
    return ' '.join(words[::-1])
if __name__ == '__main__':
    sample_sentence1 = 'Hello world! This is a test.'
    result1 = reverse_words(sample_sentence1)
    print(result1)
    sample_sentence2 = '  Word1, Word2. Word3? '
    result2 = reverse_words(sample_sentence2)
    print(result2)
    sample_sentence3 = 'Python programming is fun.'
    result3 = reverse_words(sample_sentence3)
    print(result3)