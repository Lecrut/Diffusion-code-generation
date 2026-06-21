def reverse_sentence_in_place(sentence):
    if not isinstance(sentence, str):
        raise ValueError('Input must be a string')

    def swap_characters(s, i, j):
        s[i], s[j] = (s[j], s[i])

    def reverse_word(s, start, end):
        while start < end:
            swap_characters(s, start, end)
            start += 1
            end -= 1
    chars = list(sentence)
    n = len(chars)
    reverse_word(chars, 0, n - 1)
    start = 0
    for i in range(n):
        if chars[i] == ' ':
            reverse_word(chars, start, i - 1)
            start = i + 1
    reverse_word(chars, start, n - 1)
    return ''.join(chars)
if __name__ == '__main__':
    test_cases = ['Hello world this is a test', 'Python is fun and powerful', 'Reverse this sentence', 'A quick brown fox jumps over the lazy dog', 'Keep it simple']
    for sentence in test_cases:
        try:
            reversed_sentence = reverse_sentence_in_place(sentence)
            print(reversed_sentence)
        except ValueError as e:
            print(e)