def reverse_words(s):
    words = s.split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    sentence = "  Hello   world!  This is  a test  "
    result = reverse_words(sentence)
    print(result)