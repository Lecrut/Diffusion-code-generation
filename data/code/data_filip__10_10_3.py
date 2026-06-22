def reverse_words_preserve_spacing(s: str) -> str:
    chars = list(s)
    n = len(chars)
    word_indices = []
    i = 0
    while i < n:
        if chars[i] != ' ':
            start = i
            while i < n and chars[i] != ' ':
                i += 1
            word_indices.append((start, i))
        else:
            i += 1
    
    left = 0
    right = len(word_indices) - 1
    while left < right:
        start_left, end_left = word_indices[left]
        start_right, end_right = word_indices[right]
        
        while start_left < end_left:
            chars[start_left], chars[start_right] = chars[start_right], chars[start_left]
            start_left += 1
            start_right += 1
        
        left += 1
        right -= 1
    
    return ''.join(chars)

if __name__ == '__main__':
    test_string = "  hello   world  this  is  a   test   "
    result = reverse_words_preserve_spacing(test_string)
    print(result)