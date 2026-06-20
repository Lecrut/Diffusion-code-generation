def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample = "  hello   world  foo  "
    result = reverse_words(sample)
    print(result)