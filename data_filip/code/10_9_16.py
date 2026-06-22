def reverse_words(sentence):
    words = []
    current_word = ""
    i = 0
    while i < len(sentence):
        char = sentence[i]
        if char == ' ':
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
        i += 1
    if current_word:
        words.append(current_word)
    words.reverse()
    result = ""
    for index, word in enumerate(words):
        if index > 0:
            result += ' '
        result += word
    return result

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    print(reverse_words(sample_sentence))