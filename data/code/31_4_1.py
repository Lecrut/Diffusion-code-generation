import re
def check_palindrome_with_spaces(s):
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_s == cleaned_s[::-1]
if __name__ == '__main__':
    test_string_1 = "A man, a plan, a canal: Panama"
    test_string_2 = "racecar"
    test_string_3 = "hello world"
    test_string_4 = "Madam, I'm Adam"
    test_string_5 = "No lemon, no melon"
    print(f"'{test_string_1}' is a palindrome: {check_palindrome_with_spaces(test_string_1)}")
    print(f"'{test_string_2}' is a palindrome: {check_palindrome_with_spaces(test_string_2)}")
    print(f"'{test_string_3}' is a palindrome: {check_palindrome_with_spaces(test_string_3)}")
    print(f"'{test_string_4}' is a palindrome: {check_palindrome_with_spaces(test_string_4)}")
    print(f"'{test_string_5}' is a palindrome: {check_palindrome_with_spaces(test_string_5)}")