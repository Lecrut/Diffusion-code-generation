class StringOperations:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

if __name__ == '__main__':
    sample_string = "radar"
    result = StringOperations.is_palindrome(sample_string)
    print(result)