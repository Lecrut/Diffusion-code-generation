def reverse_words_preserving_whitespace(sentence: str) -> str:
    if not sentence:
        return sentence
    
    words = []
    separators = []
    
    current_word_chars = []
    current_sep_chars = []
    
    for char in sentence:
        if char.isspace():
            if current_word_chars:
                words.append(''.join(current_word_chars))
                current_word_chars = []
            current_sep_chars.append(char)
        else:
            if current_sep_chars:
                separators.append(''.join(current_sep_chars))
                current_sep_chars = []
            current_word_chars.append(char)
    
    if current_word_chars:
        words.append(''.join(current_word_chars))
    if current_sep_chars:
        separators.append(''.join(current_sep_chars))
    
    reversed_words = words[::-1]
    
    result = []
    word_idx = 0
    sep_idx = 0
    
    for i, sep in enumerate(separators):
        if i < len(reversed_words):
            result.append(reversed_words[i])
        result.append(sep)
        
    if word_idx < len(reversed_words):
        result.append(reversed_words[len(separators)])
        
    return ''.join(result)

if __name__ == '__main__':
    text = "  Hello   world  "
    result = reverse_words_preserving_whitespace(text)
    print(result)