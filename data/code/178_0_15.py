def split_into_words(text):
    WORD_DELIMITERS = ' \t\n'
    words = []
    current_word = ''
    
    for char in text:
        if char not in WORD_DELIMITERS:
            current_word += char
        elif current_word:
            words.append(current_word.strip())
            current_word = ''
    
    if current_word:
        words.append(current_word.strip())
    
    return [word for word in words if word]

if __name__ == '__main__':
    sample_string = "   This is a test   string with  multiple spaces and punctuation! "
    result = split_into_words(sample_string)
    print(result)