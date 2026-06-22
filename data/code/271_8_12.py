def filter_palindromes(strings):
    import re
    def is_palindrome(s):
        cleaned = re.sub(r'[^a-zA-Z]', '', s).lower()
        return cleaned == cleaned[::-1]
    return [s for s in strings if is_palindrome(s)]

if __name__ == '__main__':
    sample_strings = ["Was it a car or a cat I saw?", "Madam, in Eden, I'm Adam", "Hello, World!"]
    print(filter_palindromes(sample_strings))