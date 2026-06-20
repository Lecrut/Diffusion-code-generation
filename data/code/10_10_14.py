def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return ""
    
    chars = list(s)
    n = len(chars)
    
    words = []
    i = 0
    while i < n:
        if chars[i] == ' ':
            i += 1
        else:
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            words.append(chars[i:j])
            i = j
    
    words.reverse()
    
    result = []
    i = 0
    word_idx = 0
    while i < n:
        if chars[i] == ' ':
            result.append(' ')
            i += 1
        else:
            result.append(words[word_idx])
            word_idx += 1
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            i = j
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "  hello   world  "
    sample_output = reverse_words_preserve_spacing(sample_input)
    print(sample_output)