def is_palindrome(s):
    processed = "".join(filter(str.isalnum, s)).lower()
    return processed == processed[::-1]
if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("Madam"))