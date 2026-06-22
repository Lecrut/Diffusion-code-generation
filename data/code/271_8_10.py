def filter_palindromes(strings):
    import re
    def is_palindrome(s):
        cleaned = re.sub(r'[^a-zA-Z]', '', s).lower()
        return cleaned == cleaned[::-1]
    return [s for s in strings if is_palindrome(s)]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "No lemon, no melon", "Hello, World!"]
    print(filter_palindromes(sample_strings))