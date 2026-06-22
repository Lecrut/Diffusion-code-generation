def reverse_sentence(sentence):
    return sentence[::-1]

if __name__ == '__main__':
    SAMPLE_SENTENCE = "Hello, World!"
    REVERSED_SAMPLE = "!dlroW ,olleH"
    
    original_sentence = SAMPLE_SENTENCE
    reversed_sentence = reverse_sentence(original_sentence)
    
    print(f"Original: {original_sentence}")
    print(f"Reversed: {reversed_sentence}")
    
    assert reversed_sentence == REVERSED_SAMPLE, "Test failed for the sample sentence"