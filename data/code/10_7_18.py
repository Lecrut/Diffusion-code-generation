def reverse_words(sentence: str) -> str:
    words = []
    current_word = []
    
    for char in sentence:
        if char == ' ':
            if current_word:
                words.insert(0, ''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    if current_word:
        words.insert(0, ''.join(current_word))
    
    return ' '.join(words)

if __name__ == '__main__':
    sample_sentence = "the sky is blue"
    result = reverse_words(sample_sentence)
    print(result)