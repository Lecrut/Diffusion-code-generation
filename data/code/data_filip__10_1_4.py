def reverse_words_preserve_whitespace(sentence):
    if not sentence:
        return sentence
    
    tokens = []
    current_token = ""
    is_space = None
    
    for char in sentence:
        if char.isspace():
            if is_space is False:
                if current_token:
                    tokens.append(current_token)
                current_token = ""
                is_space = True
            current_token += char
        else:
            if is_space is True:
                tokens.append(current_token)
                current_token = ""
                is_space = False
            current_token += char
    
    if current_token:
        tokens.append(current_token)
    
    word_tokens = [t for t in tokens if not t.isspace()]
    word_tokens.reverse()
    
    result_tokens = []
    word_index = 0
    
    for token in tokens:
        if token.isspace():
            result_tokens.append(token)
        else:
            result_tokens.append(word_tokens[word_index])
            word_index += 1
            
    return "".join(result_tokens)

if __name__ == '__main__':
    sample_input = "Hello   world!  This   is   a test."
    result = reverse_words_preserve_whitespace(sample_input)
    print(result)
    
    sample_input_2 = "  Leading and trailing  spaces  "
    result_2 = reverse_words_preserve_whitespace(sample_input_2)
    print(result_2)
    
    sample_input_3 = "SingleWord"
    result_3 = reverse_words_preserve_whitespace(sample_input_3)
    print(result_3)