def reverse_words(sentence):
    if not isinstance(sentence, str) or sentence.strip() == "":
        raise ValueError("Input must be a non-empty string")
    
    words = sentence.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(reverse_words(sample_sentence))