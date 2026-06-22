def reverse_words(sentence: str) -> str:
    n = len(sentence)
    if n == 0:
        return ""
    
    result = []
    word_start = None
    
    for i in range(n):
        char = sentence[i]
        if char != ' ':
            if word_start is None:
                word_start = i
        else:
            if word_start is not None:
                result.append(sentence[word_start:i])
                word_start = None
    
    if word_start is not None:
        result.append(sentence[word_start:n])
    
    reversed_words = []
    for i in range(len(result) - 1, -1, -1):
        reversed_words.append(result[i])
    
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "the sky is blue"
    print(reverse_words(sample_text))