class PalindromeFinder:
    def find_longest_palindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1

        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

            for j in range(i + 2, n):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = j - i + 1

        return s[start:start + max_length]

if __name__ == '__main__':
    pf = PalindromeFinder()
    sample_string = "babad"
    result = pf.find_longest_palindrome(sample_string)
    print(result)