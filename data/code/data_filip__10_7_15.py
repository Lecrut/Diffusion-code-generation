def reverse_words(sentence):
    result = []
    word_start = None
    for i, char in enumerate(sentence):
        if char != ' ':
            if word_start is None:
                word_start = i
        else:
            if word_start is not None:
                result.append(sentence[word_start:i])
                word_start = None
    if word_start is not None:
        result.append(sentence[word_start:])
    return ' '.join(reversed(result))

if __name__ == '__main__':
    sample = "hello world this is a test"
    reversed_sentence = reverse_words(sample)
    print(reversed_sentence)