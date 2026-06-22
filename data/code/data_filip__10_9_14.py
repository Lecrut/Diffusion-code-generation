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
    result = []
    for i, word in enumerate(words):
        result.append(word)
        if i < len(words) - 1:
            result.append(' ')
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python is great"
    sample3 = "Reverse this sentence"
    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))