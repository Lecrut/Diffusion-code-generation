def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    try:
        reversed_sentence = reverse_words(sample_sentence)
        print(reversed_sentence)
    except ValueError as e:
        print(e)