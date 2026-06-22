class StringOperations:
    @classmethod
    def is_palindrome(cls, s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_values = ["A man, a plan, a canal: Panama", "racecar", "hello", "No lemon, no melon"]
    results = {value: StringOperations.is_palindrome(value) for value in sample_values}
    print(results)