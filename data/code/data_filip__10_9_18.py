def reverse_words(sentence):
    if not sentence:
        return ""

    words = []
    current_word = []
    i = 0
    n = len(sentence)

    while i < n:
        if sentence[i] == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(sentence[i])
        i += 1

    if current_word:
        words.append(''.join(current_word))

    reversed_words = []
    i = len(words) - 1
    while i >= 0:
        reversed_words.append(words[i])
        i -= 1

    result = []
    i = 0
    n = len(reversed_words)
    while i < n:
        if i > 0:
            result.append(' ')
        result.append(reversed_words[i])
        i += 1

    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "The quick brown fox"
    sample3 = "Python"
    sample4 = ""
    sample5 = "   leading spaces"
    sample6 = "trailing spaces   "

    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))
    print(reverse_words(sample4))
    print(reverse_words(sample5))
    print(reverse_words(sample6))