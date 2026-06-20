def reverse_words_preserve_spaces(sentence):
    if not sentence:
        return sentence
    
    words = []
    spaces = []
    
    i = 0
    while i < len(sentence):
        if sentence[i] == ' ':
            count = 0
            while i < len(sentence) and sentence[i] == ' ':
                count += 1
                i += 1
            spaces.append(count)
        else:
            word = []
            while i < len(sentence) and sentence[i] != ' ':
                word.append(sentence[i])
                i += 1
            words.append(''.join(word))
            spaces.append(0)
    
    reversed_words = words[::-1]
    
    result = []
    word_idx = 0
    for space_count in spaces:
        if space_count > 0:
            result.append(' ' * space_count)
        else:
            result.append(reversed_words[word_idx])
            word_idx += 1
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello   world"
    sample2 = "  leading spaces"
    sample3 = "trailing spaces  "
    sample4 = "  multiple   spaces   between  words  "
    sample5 = "single"
    sample6 = ""
    sample7 = "   "
    
    print(reverse_words_preserve_spaces(sample1))
    print(reverse_words_preserve_spaces(sample2))
    print(reverse_words_preserve_spaces(sample3))
    print(reverse_words_preserve_spaces(sample4))
    print(reverse_words_preserve_spaces(sample5))
    print(reverse_words_preserve_spaces(sample6))
    print(reverse_words_preserve_spaces(sample7))