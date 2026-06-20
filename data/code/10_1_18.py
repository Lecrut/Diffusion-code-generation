def reverse_words_preserve_spaces(sentence):
    if not sentence:
        return sentence
    
    words = []
    spaces = []
    current_word = []
    current_spaces = []
    
    i = 0
    while i < len(sentence):
        if sentence[i] == ' ':
            current_spaces.append(sentence[i])
            i += 1
        else:
            if current_spaces:
                if current_word:
                    spaces.append(''.join(current_spaces))
                current_spaces = []
            current_word.append(sentence[i])
            i += 1
    
    if current_word:
        words.append(''.join(current_word))
    
    if not words:
        return sentence
    
    reversed_words = words[::-1]
    
    result = []
    num_spaces = len(spaces)
    for idx, word in enumerate(reversed_words):
        if idx < num_spaces:
            result.append(spaces[idx])
        result.append(word)
    
    trailing_spaces = ''
    if num_spaces > len(reversed_words):
        for i in range(len(reversed_words), num_spaces):
            trailing_spaces += spaces[i]
    
    result.append(trailing_spaces)
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "hello   world"
    sample2 = "  spaces at start"
    sample3 = "end with spaces   "
    sample4 = "  multiple   spaces   everywhere  "
    sample5 = "single"
    sample6 = ""
    sample7 = "   "
    
    print(reverse_words_preserve_spaces(sample1))
    print(reverse_words_preserve_spaces(sample2))
    print(reverse_words_preserve_spaces(sample3))
    print(reverse_words_preserve_spaces(sample4))
    print(reverse_words_preserve_spaces(sample5))
    print(reverse_words_preserve_spaces(sample6))
    print(reverse_words_preserve_spaces(sample7))