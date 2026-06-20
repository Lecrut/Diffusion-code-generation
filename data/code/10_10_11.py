def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return ""
    
    words = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == ' ':
            words.append(None)
            i += 1
        else:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            words.append(s[i:j])
            i = j
    
    left = 0
    right = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    
    result = []
    for word in words:
        if word is None:
            result.append(' ')
        else:
            result.append(word)
    
    return "".join(result)

if __name__ == '__main__':
    text = "  Hello   world  from  Python  "
    output = reverse_words_preserve_spacing(text)
    print(output)