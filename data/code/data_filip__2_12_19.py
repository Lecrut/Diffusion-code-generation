def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome("Was it a car or a cat I saw?"))