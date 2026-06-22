def reverse_words(sentence):
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
    sample_sentence = "Hello World from Python"
    result = reverse_words(sample_sentence)
    print(result)