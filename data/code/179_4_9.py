def reverse_words(sentence):
    words = [word.strip() for word in sentence.split()]
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
if __name__ == '__main__':
    sample_sentence1 = 'Hello world! This is a test.'
    result1 = reverse_words(sample_sentence1)
    print(result1)
    sample_sentence2 = "Python programming is fun, isn't it?"
    result2 = reverse_words(sample_sentence2)
    print(result2)
    sample_sentence3 = '  Spaces and punctuation matter!  '
    result3 = reverse_words(sample_sentence3)
    print(result3)