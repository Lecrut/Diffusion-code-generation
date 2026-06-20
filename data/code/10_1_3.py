def reverse_words_preserving_whitespace(sentence):
    words = sentence.split(' ')
    non_space_words = [w for w in words if w]
    reversed_words = non_space_words[::-1]
    
    result = []
    word_idx = 0
    for part in words:
        if part:
            result.append(reversed_words[word_idx])
            word_idx += 1
        else:
            result.append('')
    
    return ' '.join(result)

if __name__ == '__main__':
    text = "  Hello   world  "
    print(reverse_words_preserving_whitespace(text))