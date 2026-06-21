def reverse_words(s):
    words = []
    word = ''
    for char in s:
        if char == ' ':
            if word:
                words.append(word)
                word = ''
        else:
            word += char
    if word:
        words.append(word)
    return ' '.join(words[::-1])

if __name__ == '__main__':
    print(reverse_words("  hello   world!  "))