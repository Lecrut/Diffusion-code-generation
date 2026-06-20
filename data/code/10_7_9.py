def reverse_words(sentence):
    result = []
    current_word = []
    i = 0
    length = len(sentence)
    while i < length:
        char = sentence[i]
        if char == ' ':
            if current_word:
                result.append(''.join(reversed(current_word)))
                result.append(' ')
                current_word = []
        else:
            current_word.append(char)
        i += 1
    if current_word:
        result.append(''.join(reversed(current_word)))
    return ''.join(reversed(result))

if __name__ == '__main__':
    text = "Hello World from Python"
    output = reverse_words(text)
    print(output)