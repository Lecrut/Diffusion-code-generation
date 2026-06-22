def reverse_words(sentence):
    if not sentence:
        return ""
    reversed_chars = []
    current_word = []
    for char in reversed(sentence):
        if char == ' ':
            if current_word:
                reversed_chars.extend(reversed(current_word))
                current_word = []
            if reversed_chars and reversed_chars[-1] != ' ':
                reversed_chars.append(' ')
        else:
            current_word.append(char)
    if current_word:
        if reversed_chars and reversed_chars[-1] == ' ':
            reversed_chars.pop()
        reversed_chars.extend(reversed(current_word))
    return "".join(reversed_chars)

if __name__ == '__main__':
    sample_sentence = "the quick brown fox"
    result = reverse_words(sample_sentence)
    print(result)