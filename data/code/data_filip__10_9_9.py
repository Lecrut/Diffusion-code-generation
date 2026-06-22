def reverse_words(sentence):
    if not sentence:
        return sentence

    words = []
    current_word = []
    i = 0
    while i < len(sentence):
        if sentence[i] == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(sentence[i])
        i += 1
    if current_word:
        words.append(''.join(current_word))

    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    sample_sentence = "Hello World Python"
    result = reverse_words(sample_sentence)
    print(result)