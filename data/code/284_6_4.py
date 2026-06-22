def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    try:
        reversed_sentence = reverse_words(sample_sentence)
        print(reversed_sentence)
    except ValueError as e:
        print(e)