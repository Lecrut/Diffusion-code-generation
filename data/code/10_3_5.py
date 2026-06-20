def reverse_words_single_pass(sentence: str) -> str:
    if not sentence:
        return ''
    n = len(sentence)
    if n == 0:
        return ''

    def word_generator(text):
        start = None
        for i, char in enumerate(text):
            if char != ' ':
                if start is None:
                    start = i
            elif start is not None:
                yield text[start:i]
                start = None
        if start is not None:
            yield text[start:]
    words = list(word_generator(sentence))
    words.reverse()
    return ' '.join(words)
if __name__ == '__main__':
    result = reverse_words_single_pass('the sky is blue')
    print(result)
    result2 = reverse_words_single_pass('  hello   world  ')
    print(result2)
    result3 = reverse_words_single_pass('')
    print(result3)