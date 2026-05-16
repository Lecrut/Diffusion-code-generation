class StringOperations:
    def is_palindrome(self, text):
        processed_text = "".join(filter(str.isalnum, text)).lower()
        return processed_text == processed_text[::-1]
if __name__ == '__main__':
    so = StringOperations()
    print(so.is_palindrome("A man, a plan, a canal: Panama"))
    print(so.is_palindrome("racecar"))
    print(so.is_palindrome("hello"))
    print(so.is_palindrome("Madam"))
    print(so.is_palindrome("12321"))