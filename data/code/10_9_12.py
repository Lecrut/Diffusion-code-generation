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
    return ' '.join(words[::-1])

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words("The quick brown fox"))
    print(reverse_words("  Spaces   everywhere  "))