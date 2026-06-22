def reverse_words(sentence: str) -> str:
    if not sentence:
        return sentence
    
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
    
    return ' '.join(reversed(words))

if __name__ == '__main__':
    result = reverse_words("Hello World from Python")
    print(result)