def reverse_words(sentence: str) -> str:
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
    print(reverse_words("Hello World"))
    print(reverse_words("Python is fun"))
    print(reverse_words("  spaces  everywhere  "))
    print(reverse_words(""))
    print(reverse_words("single"))