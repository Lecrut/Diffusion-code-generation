def reverse_sentence_in_place(sentence):
    words = sentence.split()
    start, end = (0, len(words) - 1)
    while start < end:
        words[start], words[end] = (words[end], words[start])
        start += 1
        end -= 1
    return ' '.join(words)
if __name__ == '__main__':
    test_sentence = 'Hello world this is a test'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)