def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return ""
    
    words = []
    i = 0
    n = len(s)
    
    while i < n:
        while i < n and s[i] == ' ':
            i += 1
        if i >= n:
            break
        j = i
        while j < n and s[j] != ' ':
            j += 1
        words.append(s[i:j])
        i = j
    
    words.reverse()
    
    result_parts = []
    current_index = 0
    num_words = len(words)
    word_idx = 0
    
    while current_index < n:
        if word_idx < num_words:
            word = words[word_idx]
            result_parts.append(word)
            current_index += len(word)
            word_idx += 1
        else:
            result_parts.append(' ')
            current_index += 1
    
    return ''.join(result_parts)

if __name__ == '__main__':
    print(reverse_words_preserve_spacing("  hello   world  "))
    print(reverse_words_preserve_spacing("Python"))
    print(reverse_words_preserve_spacing("a b c d"))
    print(reverse_words_preserve_spacing(""))
    print(reverse_words_preserve_spacing("   "))