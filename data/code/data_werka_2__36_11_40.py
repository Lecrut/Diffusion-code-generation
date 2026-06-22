def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Python is fun and educational"
    try:
        reversed_sentence = reverse_words(sample_sentence)
        print(reversed_sentence)
    except ValueError as e:
        print(e)