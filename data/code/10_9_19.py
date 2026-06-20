def reverse_words(sentence: str) -> str:
    if not sentence:
        return ""
    
    words = []
    current_word = []
    
    for char in sentence:
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    result = reverse_words("hello world")
    print(result)