def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    def is_non_empty_string(s):
        return isinstance(s, str) and s.strip()
    
    words = sentence.split()
    if not all(is_non_empty_string(word) for word in words):
        raise ValueError("Sentence must contain only non-empty words")
    
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)