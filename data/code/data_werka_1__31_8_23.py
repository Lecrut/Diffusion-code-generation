class StringOperations:

    @staticmethod
    def is_palindrome(s):
        s = s.replace(' ', '').lower()
        return s == s[::-1]
if __name__ == '__main__':
    sample_string = 'A man a plan a canal Panama'
    result = StringOperations.is_palindrome(sample_string)
    print(result)