def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            
            if dp[i][j] and j - i + 1 > max_length:
                start = i
                max_length = j - i + 1

    return s[start:start+max_length]

if __name__ == '__main__':
    sample_string = "babad"
    result = longest_palindromic_substring(sample_string)
    print(result)