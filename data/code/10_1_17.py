def reverse_words_preserve_whitespace(sentence: str) -> str:
    words = []
    whitespaces = []
    current_word = []
    current_ws = []

    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            current_ws.append(char)
        else:
            if current_ws:
                whitespaces.append(''.join(current_ws))
                current_ws = []
            current_word.append(char)

    if current_word:
        words.append(''.join(current_word))
    if current_ws:
        whitespaces.append(''.join(current_ws))

    reversed_words = words[::-1]
    result_parts = []
    
    for i in range(len(reversed_words)):
        result_parts.append(reversed_words[i])
        if i < len(whitespaces):
            result_parts.append(whitespaces[i])
    
    if len(reversed_words) > len(whitespaces):
        result_parts.append('')
        for i in range(len(whitespaces), len(reversed_words) - 1):
            result_parts.append('')

    return ''.join(result_parts)

if __name__ == '__main__':
    sample_sentence = "  Hello   world  this   is   a   test  "
    reversed_sentence = reverse_words_preserve_whitespace(sample_sentence)
    print(reversed_sentence)