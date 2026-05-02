class StringOperations:
    def is_palindrome(self, text):
        processed_text = "".join(filter(str.isalnum, text)).lower()
        return processed_text == processed_text[::-1]
if __name__ == '__main__':
    so = StringOperations()
    test_string_1 = "A man, a plan, a canal: Panama"
    test_string_2 = "racecar"
    test_string_3 = "hello world"
    test_string_4 = "Madam"
    test_string_5 = "12321"
    print(f"'{test_string_1}' is a palindrome: {so.is_palindrome(test_string_1)}")
    print(f"'{test_string_2}' is a palindrome: {so.is_palindrome(test_string_2)}")
    print(f"'{test_string_3}' is a palindrome: {so.is_palindrome(test_string_3)}")
    print(f"'{test_string_4}' is a palindrome: {so.is_palindrome(test_string_4)}")
    print(f"'{test_string_5}' is a palindrome: {so.is_palindrome(test_string_5)}")