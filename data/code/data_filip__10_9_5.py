def reverse_words(sentence):
    words = []
    current_word = []
    for char in sentence:
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append(''.join(current_word))
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    result = reverse_words(sample_sentence)
    print(result)