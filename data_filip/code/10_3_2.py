def reverse_words_in_sentence(text: str) -> str:
    if not text:
        return text
    
    words = []
    current_word = []
    
    for char in text:
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "the sky is blue"
    result = reverse_words_in_sentence(sample_text)
    print(result)