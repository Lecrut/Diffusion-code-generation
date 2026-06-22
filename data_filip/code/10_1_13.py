def reverse_words_preserve_whitespace(sentence):
    if not sentence:
        return sentence
    words = []
    current_word = []
    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append(''.join(current_word))
    if not words:
        return sentence
    separators = []
    temp_ws = []
    for char in sentence:
        if char.isspace():
            temp_ws.append(char)
        else:
            if temp_ws:
                separators.append(''.join(temp_ws))
                temp_ws = []
    if temp_ws:
        separators.append(''.join(temp_ws))
    words.reverse()
    result = []
    word_index = 0
    sep_index = 0
    for i in range(len(separators)):
        result.append(separators[i])
        if word_index < len(words):
            result.append(words[word_index])
            word_index += 1
    if len(words) > len(separators):
        result.append(words[-1])
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "  Hello   World  test  case  "
    result = reverse_words_preserve_whitespace(sample_input)
    print(result)