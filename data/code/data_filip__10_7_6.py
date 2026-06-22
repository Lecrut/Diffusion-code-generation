def reverse_words(sentence):
    words = []
    current_word = []
    length = len(sentence)
    index = 0
    while index < length:
        char = sentence[index]
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
        index += 1
    if current_word:
        words.append(''.join(current_word))
    result = []
    count = len(words)
    i = count - 1
    while i >= 0:
        result.append(words[i])
        if i > 0:
            result.append(' ')
        i -= 1
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "Hello World from Python"
    reversed_text = reverse_words(sample_text)
    print(reversed_text)