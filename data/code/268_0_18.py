def find_initial_word(sentence):
    words = sentence.split()
    if words:
        return words[0]
    else:
        return ''
if __name__ == '__main__':
    sample_sentence = 'The quick brown fox'
    result = find_initial_word(sample_sentence)
    print(result)