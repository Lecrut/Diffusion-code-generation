def reverse_words(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    words.reverse()
    result = ""
    for i in range(len(words)):
        if i > 0:
            result += " "
        result += words[i]
    return result

if __name__ == "__main__":
    sample_sentence = "Hello world this is a test"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)