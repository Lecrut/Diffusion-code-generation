def reverse_words(s):
    if not s:
        return s
    words = []
    current_word = []
    for char in s:
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
    result = reverse_words('hello world')
    print(result)