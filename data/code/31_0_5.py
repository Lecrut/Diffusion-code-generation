def is_palindrome(s):
    processed_s = "".join(filter(str.isalnum, s)).lower()
    return processed_s == processed_s[::-1]
if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("Madam"))
    print(is_palindrome("12321"))
    print(is_palindrome("No 'x' in Nixon"))