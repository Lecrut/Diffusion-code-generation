def reverse_words(s):
    words = []
    current_word = []
    length = len(s)
    i = 0
    while i < length:
        char = s[i]
        if char != ' ':
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        i += 1
    if current_word:
        words.append(''.join(current_word))
    result = []
    j = len(words) - 1
    while j >= 0:
        result.append(words[j])
        j -= 1
    return ' '.join(result)

if __name__ == '__main__':
    sentence = "the sky is blue"
    reversed_sentence = reverse_words(sentence)
    print(reversed_sentence)