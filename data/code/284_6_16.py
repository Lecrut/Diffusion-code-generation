def reverse_words(sentence):
    if not isinstance(sentence, str) or not sentence.strip():
        raise ValueError("Input must be a non-empty string.")
    
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    try:
        reversed_sentence = reverse_words(sample_sentence)
        print(reversed_sentence)
    except ValueError as e:
        print(e)