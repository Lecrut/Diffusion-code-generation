def reverse_words_preserve_spaces(s):
    words = []
    spaces = []
    current_word = []
    current_space = []
    
    for char in s:
        if char == ' ':
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
    
    words.reverse()
    
    result = []
    word_idx = 0
    space_idx = 0
    
    if len(words) > 0 and len(spaces) > 0 and s[0] != ' ':
        result.append(words[word_idx])
        word_idx += 1
    
    for i in range(len(spaces)):
        result.append(spaces[i])
        if word_idx < len(words):
            result.append(words[word_idx])
            word_idx += 1
    
    while len(result) < len(s):
        if space_idx < len(spaces):
            result.append(spaces[space_idx])
            space_idx += 1
    
    return ''.join(result)

if __name__ == '__main__':
    test_string = "Hello   world this is  a test"
    result = reverse_words_preserve_spaces(test_string)
    print(result)
    
    test_string2 = "  one  two   three"
    result2 = reverse_words_preserve_spaces(test_string2)
    print(result2)
    
    test_string3 = "single"
    result3 = reverse_words_preserve_spaces(test_string3)
    print(result3)