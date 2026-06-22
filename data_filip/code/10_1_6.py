def reverse_words_preserve_whitespace(sentence):
    words = []
    whitespace_tokens = []
    current_word = ""
    current_whitespace = ""
    
    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(current_word)
                current_word = ""
            current_whitespace += char
        else:
            if current_whitespace:
                whitespace_tokens.append(current_whitespace)
                current_whitespace = ""
            current_word += char
    
    if current_word:
        words.append(current_word)
    if current_whitespace:
        whitespace_tokens.append(current_whitespace)
    
    words.reverse()
    
    result = []
    word_index = 0
    
    for i, token in enumerate(whitespace_tokens):
        if word_index < len(words):
            result.append(words[word_index])
            word_index += 1
        result.append(token)
    
    if word_index < len(words):
        result.append(words[word_index])
    
    return "".join(result)

if __name__ == '__main__':
    sample_sentence = "Hello   world  this is   a test"
    print(reverse_words_preserve_whitespace(sample_sentence))
    
    sample_sentence_2 = "  leading and trailing  "
    print(reverse_words_preserve_whitespace(sample_sentence_2))
    
    sample_sentence_3 = "one"
    print(reverse_words_preserve_whitespace(sample_sentence_3))
    
    sample_sentence_4 = "  "
    print(reverse_words_preserve_whitespace(sample_sentence_4))