def reverse_words_preserve_whitespace(sentence):
    if not sentence:
        return sentence

    tokens = []
    i = 0
    n = len(sentence)

    while i < n:
        if sentence[i].isspace():
            ws_start = i
            while i < n and sentence[i].isspace():
                i += 1
            tokens.append(('ws', sentence[ws_start:i]))
        else:
            word_start = i
            while i < n and not sentence[i].isspace():
                i += 1
            tokens.append(('word', sentence[word_start:i]))

    words = [token[1] for token in tokens if token[0] == 'word']
    whitespaces = [token[1] for token in tokens if token[0] == 'ws']

    words.reverse()

    result_tokens = []
    word_idx = 0
    ws_idx = 0

    for token_type, token_val in tokens:
        if token_type == 'word':
            result_tokens.append(words[word_idx])
            word_idx += 1
        else:
            result_tokens.append(token_val)
            ws_idx += 1

    return ''.join(result_tokens)

if __name__ == '__main__':
    sample1 = "Hello   World"
    sample2 = "  foo  bar  "
    sample3 = "one two three"
    sample4 = ""
    sample5 = "single"

    print(reverse_words_preserve_whitespace(sample1))
    print(reverse_words_preserve_whitespace(sample2))
    print(reverse_words_preserve_whitespace(sample3))
    print(reverse_words_preserve_whitespace(sample4))
    print(reverse_words_preserve_whitespace(sample5))