def filter_long_words(sentence):
    words = sentence.split()
    long_words = [word for word in words if len(word) > 3]
    return long_words

if __name__ == '__main__':
    sample_sentence = "Python is an interpreted, high-level and general-purpose programming language"
    result = filter_long_words(sample_sentence)
    print(result)