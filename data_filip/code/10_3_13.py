def reverse_words(s: str) -> str:
    if not s:
        return ''
    
    n = len(s)
    result = [''] * n
    current_word = []
    word_len = 0
    
    for i in range(n - 1, -1, -1):
        char = s[i]
        if char == ' ':
            if word_len > 0:
                for j in range(word_len):
                    result[n - 1 - word_len - current_word_len] = current_word[word_len - 1 - j]
                word_len = 0
                current_word = []
                current_word_len = 0
        else:
            current_word.append(char)
            word_len += 1
            current_word_len = len(current_word)
    
    if word_len > 0:
        for j in range(word_len):
            result[n - 1 - word_len - current_word_len] = current_word[word_len - 1 - j]
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "the sky is blue"
    output = reverse_words(sample_input)
    print(output)