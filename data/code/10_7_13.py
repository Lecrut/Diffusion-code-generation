def reverse_words(sentence):
    result = []
    current_word = []
    for char in sentence:
        if char == ' ':
            if current_word:
                result.append(''.join(reversed(current_word)))
                current_word = []
            result.append(' ')
        else:
            current_word.append(char)
    if current_word:
        result.append(''.join(reversed(current_word)))
    return ''.join(result)

if __name__ == '__main__':
    sample = "hello world"
    print(reverse_words(sample))