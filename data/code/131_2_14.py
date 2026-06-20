class PalindromeFinder:

    @staticmethod
    def longest_palindromic_substring(s):
        n = len(s)
        if n == 0:
            return ''
        start, max_length = (0, 1)
        for i in range(n):
            low = i
            high = i
            while low >= 0 and high < n and (s[low] == s[high]):
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1
            low = i
            high = i + 1
            while low >= 0 and high < n and (s[low] == s[high]):
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1
        return s[start:start + max_length]
if __name__ == '__main__':
    finder = PalindromeFinder()
    sample_string = 'babad'
    result = finder.longest_palindromic_substring(sample_string)
    print(result)