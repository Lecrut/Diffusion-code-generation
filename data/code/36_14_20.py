def reverse_sentence_in_place(sentence):
    words = sentence.split()
    left, right = (0, len(words) - 1)
    while left < right:
        words[left], words[right] = (words[right], words[left])
        left += 1
        right -= 1
    return ' '.join(words)
if __name__ == '__main__':
    test_sentence = 'Hello world this is a test'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)