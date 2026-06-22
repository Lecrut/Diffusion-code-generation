def reverse_words(sentence):
    words = []
    current_word = []
    length = len(sentence)
    for char in sentence:
        if char != ' ':
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
    if current_word:
        words.append(''.join(current_word))
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    text = "Hello World from Python"
    result = reverse_words(text)
    print(result)