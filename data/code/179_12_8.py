def reverse_word_order(sentence):
    if not isinstance(sentence, str) or not sentence.strip():
        raise ValueError("Input must be a non-empty string")
    
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(reverse_word_order(sample_sentence))