import re

class PalindromeFilter:
    @staticmethod
    def is_palindrome(s):
        cleaned = re.sub(r'[^a-zA-Z]', '', s).lower()
        return cleaned == cleaned[::-1]

    @classmethod
    def filter_palindromes(cls, strings):
        return [s for s in strings if cls.is_palindrome(s)]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "race a car", "No lemon, no melon"]
    print(PalindromeFilter.filter_palindromes(sample_strings))