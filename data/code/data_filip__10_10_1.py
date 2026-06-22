def reverse_words_preserving_spacing(s):
    n = len(s)
    if n == 0:
        return s
    
    words = []
    i = 0
    while i < n:
        if s[i] != ' ':
            j = i
            while j < n and s[j] != ' ':
                j += 1
            words.append(s[i:j])
            i = j
        else:
            i += 1
    
    if len(words) == 0:
        return s
    
    reversed_words = words[::-1]
    
    result = []
    word_idx = 0
    i = 0
    while i < n:
        if s[i] == ' ':
            j = i
            while j < n and s[j] == ' ':
                j += 1
            result.append(s[i:j])
            i = j
        else:
            if word_idx < len(reversed_words):
                result.append(reversed_words[word_idx])
                word_idx += 1
            j = i
            while j < n and s[j] != ' ':
                j += 1
            i = j
    
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "  Hello   world!  This  is   a   test  "
    result = reverse_words_preserving_spacing(sample_string)
    print(result)