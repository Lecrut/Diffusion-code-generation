def reverse_words_preserve_whitespace(sentence: str) -> str:
    if not sentence:
        return sentence
    
    words = []
    spaces = []
    current_word = []
    current_space = []
    in_word = sentence[0].isalpha() or sentence[0].isdigit() or sentence[0] in "_-"
    
    for char in sentence:
        is_alpha_num = char.isalpha() or char.isdigit() or char in "_-"
        if is_alpha_num == in_word:
            if is_alpha_num:
                current_word.append(char)
            else:
                current_space.append(char)
        else:
            if is_alpha_num:
                if current_space:
                    spaces.append(''.join(current_space))
                    current_space = []
                words.append(''.join(current_word))
                current_word = [char]
                in_word = True
            else:
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
                current_space = [char]
                in_word = False
    
    if current_word:
        words.append(''.join(current_word))
    elif current_space:
        spaces.append(''.join(current_space))
    
    words.reverse()
    
    result = []
    space_idx = 0
    word_idx = 0
    
    if sentence and not (sentence[0].isalpha() or sentence[0].isdigit() or sentence[0] in "_-"):
        if space_idx < len(spaces):
            result.append(spaces[space_idx])
            space_idx += 1
    
    while word_idx < len(words) and space_idx < len(spaces):
        result.append(words[word_idx])
        word_idx += 1
        result.append(spaces[space_idx])
        space_idx += 1
    
    if word_idx < len(words):
        result.append(words[word_idx])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_sentence = "  Hello   world  this is  a   test"
    reversed_sentence = reverse_words_preserve_whitespace(sample_sentence)
    print(reversed_sentence)