def find_first_word(s):
    word_lengths = {' ': 0}
    current_word_length = 0
    
    for char in s:
        if char == ' ':
            if current_word_length > 0:
                break
        else:
            current_word_length += 1
            
    return s[:current_word_length]

if __name__ == '__main__':
    sample_string = "Hello world"
    print(find_first_word(sample_string))