def reverse_sentence_in_place(sentence):

    def reverse_substring(s, start, end):
        while start < end:
            s[start], s[end] = (s[end], s[start])
            start += 1
            end -= 1
    chars = list(sentence)
    reverse_substring(chars, 0, len(chars) - 1)
    start = 0
    while start < len(chars):
        if chars[start] == ' ':
            start += 1
            continue
        end = start
        while end < len(chars) and chars[end] != ' ':
            end += 1
        reverse_substring(chars, start, end - 1)
        start = end + 1
    return ''.join(chars)
if __name__ == '__main__':
    test_sentence = 'A quick brown fox jumps over the lazy dog'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)