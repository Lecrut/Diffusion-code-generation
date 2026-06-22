def reverse_sentence_in_place(sentence):

    def reverse_chars(s, start, end):
        while start < end:
            s[start], s[end] = (s[end], s[start])
            start += 1
            end -= 1
    chars = list(sentence)
    reverse_chars(chars, 0, len(chars) - 1)
    start = 0
    while start < len(chars):
        if chars[start] != ' ':
            end = start
            while end < len(chars) and chars[end] != ' ':
                end += 1
            reverse_chars(chars, start, end - 1)
            start = end
        else:
            start += 1
    return ''.join(chars)
if __name__ == '__main__':
    test_sentence = 'Hello World'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)