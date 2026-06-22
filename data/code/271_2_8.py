def is_palindrome(s):
    alpha_chars = [char.lower() for char in s if char.isalpha()]
    return alpha_chars == alpha_chars[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))