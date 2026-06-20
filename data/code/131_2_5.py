def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True

    for end in range(2, n + 1):
        for start in range(end - 1, -1, -1):
            if s[start] == s[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    if end - start + 1 > max_len:
                        max_len = end - start + 1

    return s[start:start + max_len]

if __name__ == '__main__':
    sample_string = "babad"
    print(longest_palindromic_substring(sample_string))