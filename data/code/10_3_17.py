def reverse_words(s: str) -> str:
    if not s:
        return ""
    
    length = len(s)
    words = []
    start = 0
    
    for i in range(length + 1):
        if i == length or s[i] == ' ':
            if i > start:
                words.append(s[start:i])
            start = i + 1
    
    if not words:
        return ""
    
    result = words[-1]
    for i in range(len(words) - 2, -1, -1):
        result += ' ' + words[i]
    
    return result

if __name__ == '__main__':
    sample_text = "the sky is blue"
    result = reverse_words(sample_text)
    print(result)