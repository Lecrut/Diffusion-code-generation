def reverse_sentence_in_place(sentence):

    def reverse_list(s, start, end):
        while start < end:
            s[start], s[end] = (s[end], s[start])
            start += 1
            end -= 1
    char_list = list(sentence)
    reverse_list(char_list, 0, len(char_list) - 1)
    start = 0
    for end in range(len(char_list)):
        if char_list[end] == ' ':
            reverse_list(char_list, start, end - 1)
            start = end + 1
    reverse_list(char_list, start, len(char_list) - 1)
    return ''.join(char_list)
if __name__ == '__main__':
    test_sentence = 'Hello World'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)