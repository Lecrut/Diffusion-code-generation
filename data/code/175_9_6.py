def split_and_reverse(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = sentence.split()
    reversed_words = words[::-1]
    return reversed_words

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    result = split_and_reverse(sample_sentence)
    print(result)