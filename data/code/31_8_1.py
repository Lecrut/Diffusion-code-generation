class StringOperations:
    def is_palindrome(self, text):
        cleaned_text = "".join(filter(str.isalnum, text)).lower()
        return cleaned_text == cleaned_text[::-1]
if __name__ == '__main__':
    sorter = StringOperations()
    test_string_1 = "A man, a plan, a canal: Panama"
    test_string_2 = "racecar"
    test_string_3 = "hello world"
    test_string_4 = "Madam"
    test_string_5 = "No lemon, no melon"
    print(f"'{test_string_1}' is a palindrome: {sorter.is_palindrome(test_string_1)}")
    print(f"'{test_string_2}' is a palindrome: {sorter.is_palindrome(test_string_2)}")
    print(f"'{test_string_3}' is a palindrome: {sorter.is_palindrome(test_string_3)}")
    print(f"'{test_string_4}' is a palindrome: {sorter.is_palindrome(test_string_4)}")
    print(f"'{test_string_5}' is a palindrome: {sorter.is_palindrome(test_string_5)}")