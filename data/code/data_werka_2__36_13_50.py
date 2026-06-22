def reverse_sentence_in_place(sentence):

    def reverse_range(chars, start, end):
        while start < end:
            chars[start], chars[end] = (chars[end], chars[start])
            start += 1
            end -= 1
    if not sentence:
        return sentence
    chars = list(sentence)
    n = len(chars)
    reverse_range(chars, 0, n - 1)
    start = 0
    for end in range(n):
        if chars[end] == ' ':
            reverse_range(chars, start, end - 1)
            start = end + 1
    reverse_range(chars, start, n - 1)
    return ''.join(chars)
if __name__ == '__main__':
    test_cases = ['Hello world this is a test', 'Python is fun and powerful', 'Reverse this sentence', 'A quick brown fox', 'Keep it simple']
    for sentence in test_cases:
        reversed_sentence = reverse_sentence_in_place(sentence)
        print(reversed_sentence)