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
    result = []
    for i in range(len(words) - 1, -1, -1):
        if result:
            result.append(' ')
        result.extend(words[i])
    return ''.join(result)

if __name__ == '__main__':
    sample = "Hello World from Python"
    print(reverse_words(sample))