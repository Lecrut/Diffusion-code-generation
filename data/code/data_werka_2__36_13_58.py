def reverse_sentence_in_place(sentence):

    def swap_characters(s, i, j):
        s[i], s[j] = (s[j], s[i])
    chars = list(sentence)
    n = len(chars)
    start, end = (0, n - 1)
    while start < end:
        swap_characters(chars, start, end)
        start += 1
        end -= 1
    start = 0
    for i in range(n):
        if chars[i] == ' ' or i == n - 1:
            end = i if i != n - 1 else i + 1
            while start < end:
                swap_characters(chars, start, end - 1)
                start += 1
                end -= 1
            start = i + 1
    return ''.join(chars)
if __name__ == '__main__':
    test_cases = ['Hello world this is a test', 'Python is fun and powerful', 'Reverse this sentence', 'A quick brown fox jumps over the lazy dog', 'Keep it simple']
    for sentence in test_cases:
        reversed_sentence = reverse_sentence_in_place(sentence)
        print(reversed_sentence)