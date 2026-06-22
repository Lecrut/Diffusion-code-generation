class StringOperations:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "level", "world"]
    for string in sample_strings:
        result = StringOperations.is_palindrome(string)
        print(f"'{string}' is a palindrome: {result}")