def reverse_words_preserve_spaces(sentence):
    if not sentence:
        return sentence
    
    tokens = []
    i = 0
    n = len(sentence)
    
    while i < n:
        if sentence[i].isspace():
            spaces = []
            while i < n and sentence[i].isspace():
                spaces.append(sentence[i])
                i += 1
            tokens.append(('space', ''.join(spaces)))
        else:
            words = []
            while i < n and not sentence[i].isspace():
                words.append(sentence[i])
                i += 1
            tokens.append(('word', ''.join(words)))
    
    word_tokens = [t for t in tokens if t[0] == 'word']
    word_tokens.reverse()
    
    result = []
    word_idx = 0
    for token_type, token_value in tokens:
        if token_type == 'word':
            result.append(word_tokens[word_idx][1])
            word_idx += 1
        else:
            result.append(token_value)
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello   World"
    sample2 = "  Leading spaces"
    sample3 = "Trailing spaces   "
    sample4 = "  Multiple   spaces   between  words  "
    sample5 = "Single"
    sample6 = ""
    sample7 = "   "
    sample8 = "A B C D"
    
    print(reverse_words_preserve_spaces(sample1))
    print(reverse_words_preserve_spaces(sample2))
    print(reverse_words_preserve_spaces(sample3))
    print(reverse_words_preserve_spaces(sample4))
    print(reverse_words_preserve_spaces(sample5))
    print(reverse_words_preserve_spaces(sample6))
    print(reverse_words_preserve_spaces(sample7))
    print(reverse_words_preserve_spaces(sample8))