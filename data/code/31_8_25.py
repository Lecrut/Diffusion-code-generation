class StringOperations:

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
if __name__ == '__main__':
    test_string = 'radar'
    result = StringOperations.is_palindrome(test_string)
    print(result)
    test_string2 = 'hello'
    result2 = StringOperations.is_palindrome(test_string2)
    print(result2)