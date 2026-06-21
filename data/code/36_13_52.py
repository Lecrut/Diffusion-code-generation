def reverse_sentence_in_place(sentence):

    def is_valid_sentence(s):
        return isinstance(s, str) and len(s) > 0
    if not is_valid_sentence(sentence):
        raise ValueError('Input must be a non-empty string')
    chars = list(sentence)

    def reverse_range(start, end):
        while start < end:
            chars[start], chars[end] = (chars[end], chars[start])
            start += 1
            end -= 1
    reverse_range(0, len(chars) - 1)
    start = 0
    for end in range(len(chars)):
        if chars[end] == ' ':
            reverse_range(start, end - 1)
            start = end + 1
    reverse_range(start, len(chars) - 1)
    return ''.join(chars)
if __name__ == '__main__':
    test_cases = ['Hello world this is a test', 'Python is fun and powerful', 'Reverse this sentence', 'A quick brown fox jumps over the lazy dog']
    for sentence in test_cases:
        reversed_sentence = reverse_sentence_in_place(sentence)
        print(reversed_sentence)