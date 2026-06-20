def reverse_words_preserving_whitespace(sentence):
    if not sentence:
        return ""
    words = []
    spaces = []
    current_word = []
    current_space = []
    
    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            current_space.append(char)
        else:
            if current_space:
                spaces.append(''.join(current_space))
                current_space = []
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    if current_space:
        spaces.append(''.join(current_space))
    
    if not words:
        return sentence
    
    words.reverse()
    
    result = []
    word_index = 0
    space_index = 0
    
    while word_index < len(words) or space_index < len(spaces):
        if space_index < len(spaces):
            result.append(spaces[space_index])
            space_index += 1
        if word_index < len(words):
            result.append(words[word_index])
            word_index += 1
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello   world  this  is   a  test"
    result = reverse_words_preserving_whitespace(sample_input)
    print(result)
    sample_input_2 = "  leading and trailing  "
    result_2 = reverse_words_preserving_whitespace(sample_input_2)
    print(result_2)
    sample_input_3 = "Single"
    result_3 = reverse_words_preserving_whitespace(sample_input_3)
    print(result_3)