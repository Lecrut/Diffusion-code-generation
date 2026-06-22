def reverse_words_in_sentence(sentence):
    if not sentence:
        return ''
    result = []
    n = len(sentence)
    start = 0
    while start < n:
        while start < n and sentence[start] == ' ':
            start += 1
        if start == n:
            break
        end = start
        while end < n and sentence[end] != ' ':
            end += 1
        word = sentence[start:end]
        result.append(word)
        start = end
    result.reverse()
    return ' '.join(result)
if __name__ == '__main__':
    input_sentence = 'the sky is blue'
    output = reverse_words_in_sentence(input_sentence)
    print(output)