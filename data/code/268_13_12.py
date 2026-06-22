def extract_first_word(sentence):
    if not sentence:
        raise ValueError("Input string cannot be empty")
    
    word = ''
    found_space = False
    
    for char in sentence:
        if char == ' ' and not found_space:
            break
        elif char != ' ':
            word += char
            found_space = True
        else:
            continue
    
    return word

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))