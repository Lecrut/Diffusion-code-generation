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
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_words("hello world"))
    print(reverse_words("python programming"))
    print(reverse_words("a"))
    print(reverse_words(""))
    print(reverse_words("  leading spaces "))
    print(reverse_words("trailing spaces  "))
    print(reverse_words("  multiple   spaces   here  "))