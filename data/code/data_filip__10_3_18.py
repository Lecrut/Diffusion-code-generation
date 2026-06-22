def reverse_words_in_place(sentence: str) -> str:
    if not sentence:
        return ""
    
    chars = list(sentence)
    n = len(chars)
    left = 0
    
    for right in range(n + 1):
        if right == n or chars[right] == ' ':
            end = right - 1
            while left < end:
                chars[left], chars[end] = chars[end], chars[left]
                left += 1
                end -= 1
            left = right + 1
            
    return "".join(chars)

if __name__ == '__main__':
    text = "the quick brown fox"
    result = reverse_words_in_place(text)
    print(result)