def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start = 0

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start + max_len]

if __name__ == '__main__':
    sample_string = "babad"
    result = longest_palindromic_substring(sample_string)
    print(result)