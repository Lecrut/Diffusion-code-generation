def is_unique_chars(s: str) -> bool:
    n = len(s)
    if n == 0:
        return True
    if n == 1:
        return True
    
    chars = []
    i = 0
    while i < n:
        chars.append(s[i])
        i += 1
    
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if chars[i] > chars[j]:
                temp = chars[i]
                chars[i] = chars[j]
                chars[j] = temp
            j += 1
        i += 1
    
    i = 1
    while i < n:
        if chars[i] == chars[i - 1]:
            return False
        i += 1
    
    return True

if __name__ == '__main__':
    sample = "abcdefg"
    result = is_unique_chars(sample)
    print(result)
    
    sample2 = "hello"
    result2 = is_unique_chars(sample2)
    print(result2)