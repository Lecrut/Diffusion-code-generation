def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    table = [[False] * n for _ in range(n)]
    start, max_len = 0, 1
    
    for i in range(n):
        table[i][i] = True
        
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            max_len = 2
    
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and table[i + 1][j - 1]:
                table[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

if __name__ == '__main__':
    sample_string = "babad"
    result = longest_palindrome(sample_string)
    print(result)