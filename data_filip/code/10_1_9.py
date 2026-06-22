import re

def reverse_words_preserve_whitespace(sentence):
    if not sentence:
        return sentence
    
    tokens = []
    current_word = []
    current_space = []
    
    for char in sentence:
        if char.isspace():
            if current_word:
                tokens.append(('word', ''.join(current_word)))
                current_word = []
            current_space.append(char)
        else:
            if current_space:
                tokens.append(('space', ''.join(current_space)))
                current_space = []
            current_word.append(char)
    
    if current_word:
        tokens.append(('word', ''.join(current_word)))
    if current_space:
        tokens.append(('space', ''.join(current_space)))
    
    word_indices = [i for i, t in enumerate(tokens) if t[0] == 'word']
    word_values = [t[1] for t in tokens if t[0] == 'word']
    
    reversed_words = word_values[::-1]
    
    result_tokens = []
    word_counter = 0
    
    for token_type, token_value in tokens:
        if token_type == 'word':
            result_tokens.append(reversed_words[word_counter])
            word_counter += 1
        else:
            result_tokens.append(token_value)
    
    return ''.join(result_tokens)

if __name__ == '__main__':
    sample_input = "Hello   World!  Python is  Great"
    result = reverse_words_preserve_whitespace(sample_input)
    print(result)
    sample_input2 = "  leading and trailing  "
    result2 = reverse_words_preserve_whitespace(sample_input2)
    print(result2)
    sample_input3 = "single"
    result3 = reverse_words_preserve_whitespace(sample_input3)
    print(result3)