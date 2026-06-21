def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    words = sentence.split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    sample_sentence = "Python is great for programming"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)