def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_text = "  Hello   world  this   is   a  test  "
    result = reverse_words(sample_text)
    print(result)