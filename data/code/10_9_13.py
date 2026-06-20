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
    
    reversed_words = []
    index = len(words) - 1
    while index >= 0:
        reversed_words.append(words[index])
        index -= 1
    
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    result = reverse_words(sample_sentence)
    print(result)