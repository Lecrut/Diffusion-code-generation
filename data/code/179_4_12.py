def clean_and_reverse(sentence):
    words = [word.strip() for word in sentence.split()]
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_sentence1 = "Hello world! This is a test."
    result1 = clean_and_reverse(sample_sentence1)
    print(result1)

    sample_sentence2 = "  Python programming is fun, isn't it?  "
    result2 = clean_and_reverse(sample_sentence2)
    print(result2)

    sample_sentence3 = "Word1, Word2. Word3? "
    result3 = clean_and_reverse(sample_sentence3)
    print(result3)