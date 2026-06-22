class StringOperations:

    @staticmethod
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
if __name__ == '__main__':
    test_strings = ['racecar', 'hello', 'level', 'world', 'madam']
    for string in test_strings:
        result = StringOperations.is_palindrome(string)
        print(f"'{string}' is a palindrome: {result}")