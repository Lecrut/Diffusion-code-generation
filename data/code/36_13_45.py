def reverse_sentence_in_place(sentence):
    if not isinstance(sentence, list):
        raise ValueError('Input must be a list of characters')

    def reverse_range(start, end):
        while start < end:
            sentence[start], sentence[end] = (sentence[end], sentence[start])
            start += 1
            end -= 1
    n = len(sentence)
    reverse_range(0, n - 1)
    start = 0
    for end in range(n):
        if sentence[end] == ' ':
            reverse_range(start, end - 1)
            start = end + 1
    reverse_range(start, n - 1)
if __name__ == '__main__':
    sentence = list('Hello World')
    reverse_sentence_in_place(sentence)
    print(''.join(sentence))