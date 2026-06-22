def get_first_word(sentence):
    words = sentence.split()
    if words:
        return words[0]
    else:
        return ""

if __name__ == '__main__':
    sample_sentence = "The quick brown fox"
    result = get_first_word(sample_sentence)
    print(result)