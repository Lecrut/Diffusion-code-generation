def reverse_words(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char == ' ':
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    reversed_words = []
    index = len(words) - 1
    while index >= 0:
        reversed_words.append(words[index])
        index -= 1
    result = ""
    for i, word in enumerate(reversed_words):
        result += word
        if i < len(reversed_words) - 1:
            result += " "
    return result

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    print(reverse_words(sample_sentence))