def reverse_words_in_place(sentence: str) -> str:
    chars = list(sentence)
    n = len(chars)
    start = 0
    
    while start < n:
        end = start
        while end < n and chars[end] != ' ':
            end += 1
        
        left, right = start, end - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        start = end + 1
    
    start = 0
    while start < n:
        if chars[start] == ' ':
            start += 1
            continue
        
        end = start
        while end < n and chars[end] != ' ':
            end += 1
        
        left, right = start, end - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        start = end
    
    result = ''.join(chars)
    return result

if __name__ == '__main__':
    sentence = "the quick brown fox"
    result = reverse_words_in_place(sentence)
    print(result)