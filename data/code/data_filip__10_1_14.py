def reverse_words_with_whitespace(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    
    spaces = []
    for char in sentence:
        if char == ' ':
            spaces.append(char)
        else:
            spaces.append('')
            
    result = []
    word_idx = 0
    space_idx = 0
    space_count = len(spaces)
    word_count = len(reversed_words)
    
    i = 0
    while i < len(sentence):
        if spaces[i]:
            result.append(spaces[i])
            space_idx += 1
        else:
            result.append(reversed_words[word_idx])
            word_idx += 1
        i += 1
        
    return ''.join(result)

if __name__ == '__main__':
    print(reverse_words_with_whitespace("Hello   World"))
    print(reverse_words_with_whitespace("  Spaces  at  start  "))
    print(reverse_words_with_whitespace("Single"))