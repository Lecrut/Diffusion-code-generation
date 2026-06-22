def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return ""

    words = []
    current_word_start = -1
    
    n = len(s)
    i = 0
    while i < n:
        if s[i] != ' ':
            if current_word_start == -1:
                current_word_start = i
            i += 1
        else:
            if current_word_start != -1:
                words.append(s[current_word_start:i])
                current_word_start = -1
            i += 1
            
    if current_word_start != -1:
        words.append(s[current_word_start:i])
        
    reversed_words = words[::-1]
    
    result = []
    original_word_starts = []
    original_word_ends = []
    
    current_start = 0
    for word in words:
        original_word_starts.append(current_start)
        original_word_ends.append(current_start + len(word))
        current_start += len(word)
        
    result_str = ""
    word_idx = 0
    s_idx = 0
    n = len(s)
    
    while s_idx < n:
        if s[s_idx] == ' ':
            result_str += ' '
            s_idx += 1
        else:
            if word_idx < len(reversed_words):
                result_str += reversed_words[word_idx]
                word_idx += 1
                s_idx += 1
                
    return result_str

if __name__ == '__main__':
    sample_string = "  hello   world  "
    output = reverse_words_preserve_spacing(sample_string)
    print(repr(output))
    
    sample_string_2 = "a   b  c d"
    output_2 = reverse_words_preserve_spacing(sample_string_2)
    print(repr(output_2))
    
    sample_string_3 = "single"
    output_3 = reverse_words_preserve_spacing(sample_string_3)
    print(repr(output_3))
    
    sample_string_4 = "   "
    output_4 = reverse_words_preserve_spacing(sample_string_4)
    print(repr(output_4))