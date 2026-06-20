def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample = "  This   is  a  test  string   "
    result = reverse_words(sample)
    print(result)