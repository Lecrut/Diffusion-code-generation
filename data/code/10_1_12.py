def reverse_words_preserving_whitespace(sentence):
    if not sentence:
        return sentence

    words = sentence.split()
    words.reverse()

    whitespace_indices = []
    current_space = []
    for char in sentence:
        if char.isspace():
            current_space.append(char)
        else:
            if current_space:
                whitespace_indices.append(''.join(current_space))
                current_space = []
    if current_space:
        whitespace_indices.append(''.join(current_space))

    if not whitespace_indices:
        return ' '.join(words)

    result_parts = []
    word_index = 0
    ws_index = 0

    for i, char in enumerate(sentence):
        if char.isspace():
            continue
        
        if word_index < len(words):
            result_parts.append(words[word_index])
            word_index += 1
            
            if word_index < len(words):
                if ws_index < len(whitespace_indices):
                    result_parts.append(whitespace_indices[ws_index])
                    ws_index += 1

    return ''.join(result_parts)

if __name__ == '__main__':
    input_text = "  Hello   world  "
    result = reverse_words_preserving_whitespace(input_text)
    print(repr(result))