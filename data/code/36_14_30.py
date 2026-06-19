def reverse_sentence_in_place(sentence):
    chars = list(sentence)

    def reverse_range(start, end):
        while start < end:
            chars[start], chars[end] = (chars[end], chars[start])
            start += 1
            end -= 1
    reverse_range(0, len(chars) - 1)
    start = 0
    while start < len(chars):
        if chars[start] != ' ':
            end = start
            while end + 1 < len(chars) and chars[end + 1] != ' ':
                end += 1
            reverse_range(start, end)
            start = end + 1
        else:
            start += 1
    return ''.join(chars)
if __name__ == '__main__':
    test_sentence = 'Hello World'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)