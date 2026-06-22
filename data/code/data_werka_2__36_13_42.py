def reverse_sentence_in_place(sentence):

    def reverse_list(lst, start, end):
        while start < end:
            lst[start], lst[end] = (lst[end], lst[start])
            start += 1
            end -= 1
    words = sentence.split()
    for i in range(len(words)):
        words[i] = ''.join(reverse_list(list(words[i]), 0, len(words[i]) - 1))
    reverse_list(words, 0, len(words) - 1)
    return ' '.join(words)
if __name__ == '__main__':
    test_sentence = 'Hello world this is a test'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)