def reverse_words_preserving_spacing(s: str) -> str:
    words = s.split(' ')
    words_reversed = [word for word in words if word != ''][::-1]
    
    result_parts = []
    word_idx = 0
    
    i = 0
    while i < len(s):
        if s[i] == ' ':
            count = 0
            while i < len(s) and s[i] == ' ':
                count += 1
                i += 1
            result_parts.append(' ' * count)
        else:
            if word_idx < len(words_reversed):
                result_parts.append(words_reversed[word_idx])
                word_idx += 1
            while i < len(s) and s[i] != ' ':
                i += 1
    
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_input = "  hello   world  "
    sample_output = reverse_words_preserving_spacing(sample_input)
    print(sample_output)