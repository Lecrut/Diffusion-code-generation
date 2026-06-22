def reverse_words(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word != "":
        words.append(current_word)
    reversed_words = []
    i = len(words) - 1
    while i >= 0:
        reversed_words.append(words[i])
        i -= 1
    result = ""
    j = 0
    while j < len(reversed_words):
        result += reversed_words[j]
        if j < len(reversed_words) - 1:
            result += " "
        j += 1
    return result

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    print(reverse_words(sample_sentence))