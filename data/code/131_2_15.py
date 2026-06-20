def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1
    
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            
            if dp[i][j] and length > max_len:
                start = i
                max_len = length
    
    return s[start:start + max_len]

if __name__ == '__main__':
    sample_string = "babad"
    result = longest_palindromic_substring(sample_string)
    print(result)