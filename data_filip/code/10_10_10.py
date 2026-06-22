def reverse_words_preserve_spacing(s: str) -> str:
    words = []
    current_word = []
    
    for char in s:
        if char != ' ':
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
    
    if current_word:
        words.append(''.join(current_word))
    
    words.reverse()
    
    result = []
    left = 0
    right = len(s) - 1
    
    if not words:
        return s
    
    left_space = 0
    while left < len(s) and s[left] != ' ':
        left += 1
        left_space += 1
    
    right_space = 0
    while right >= 0 and s[right] != ' ':
        right -= 1
        right_space += 1
    
    result.extend([' '] * left_space)
    
    for i in range(len(words) - 1):
        result.append(words[i])
        next_space_start = left_space
        while next_space_start < len(s) and s[next_space_start] == ' ':
            next_space_start += 1
        next_space_end = next_space_start
        while next_space_end < len(s) and s[next_space_end] != ' ':
            next_space_end += 1
        spaces_between = next_space_start - next_space_end + (next_space_end - next_space_start)
        
        actual_spaces = next_space_end - next_space_start
        result.extend([' '] * actual_spaces)
        left_space += 1 + actual_spaces
        while left_space < len(s) and s[left_space] == ' ':
            left_space += 1
    
    last_word_space_count = 0
    check_idx = len(s) - 1 - right_space
    while check_idx >= 0 and s[check_idx] == ' ':
        last_word_space_count += 1
        check_idx -= 1
    
    if last_word_space_count > 0:
        result.extend([' '] * last_word_space_count)
    
    result.append(words[-1])
    
    return ''.join(result)

if __name__ == '__main__':
    sample = "  hello   world  foo  "
    res = reverse_words_preserve_spacing(sample)
    print(repr(res))