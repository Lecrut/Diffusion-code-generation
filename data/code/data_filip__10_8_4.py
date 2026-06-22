def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_input = "Python is a high-level programming language"
    result = reverse_words(sample_input)
    print(result)