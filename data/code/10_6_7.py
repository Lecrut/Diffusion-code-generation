def reverse_words(text):
    words = text.split(' ')
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        if words[i] != '':
            reversed_words.append(words[i])
        elif i < len(words) - 1:
            reversed_words.append('')
    return ' '.join(reversed_words).rstrip(' ')

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words("The quick brown fox"))
    print(reverse_words("Python is awesome"))