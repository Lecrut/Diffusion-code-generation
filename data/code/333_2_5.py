def get_first_letters(sentence):
    return [word[0] for word in sentence.split() if word]
if __name__ == '__main__':
    sample_sentence = "Python is a powerful programming language."
    result = get_first_letters(sample_sentence)
    print("".join(result))