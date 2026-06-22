def reverse_words_preserving_spacing(s: str) -> str:
    n = len(s)
    if n == 0:
        return s
    
    words = []
    spaces = []
    
    i = 0
    while i < n:
        if s[i] == ' ':
            space_count = 0
            while i < n and s[i] == ' ':
                space_count += 1
                i += 1
            spaces.append(space_count)
        else:
            word_start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[word_start:i])
    
    if not words:
        return s
    
    words.reverse()
    spaces.reverse()
    
    result = []
    word_idx = 0
    space_idx = 0
    
    while word_idx < len(words):
        result.append(words[word_idx])
        word_idx += 1
        
        if space_idx < len(spaces):
            result.append(' ' * spaces[space_idx])
            space_idx += 1
    
    while space_idx < len(spaces):
        result.append(' ' * spaces[space_idx])
        space_idx += 1
    
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "Hello   World  Python"
    reversed_text = reverse_words_preserving_spacing(sample_text)
    print(reversed_text)