def has_long_word(sentence):
    words = sentence.split()
    for word in words:
        if len(word) > 6:
            return True
    return False
if __name__ == '__main__':
    sample_sentence1 = 'This is a test sentence with some longwords.'
    print(f'Sample 1: {has_long_word(sample_sentence1)}')
    sample_sentence2 = 'Short words only here.'
    print(f'Sample 2: {has_long_word(sample_sentence2)}')