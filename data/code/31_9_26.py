def is_palindrome(s):
    return s.lower() == s[::-1].lower()
if __name__ == '__main__':
    print(is_palindrome('Racecar'))
    print(is_palindrome('Hello'))
    print(is_palindrome('A man a plan a canal Panama'))