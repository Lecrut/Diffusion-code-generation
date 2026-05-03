import sys
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    test_string_3 = "madam"
    test_string_4 = "A man a plan a canal Panama"
    print(f"Testing '{test_string_1}': {'Palindrome' if is_palindrome(test_string_1) else 'Not a Palindrome'}")
    print(f"Testing '{test_string_2}': {'Palindrome' if is_palindrome(test_string_2) else 'Not a Palindrome'}")
    print(f"Testing '{test_string_3}': {'Palindrome' if is_palindrome(test_string_3) else 'Not a Palindrome'}")
    print(f"Testing '{test_string_4}': {'Palindrome' if is_palindrome(test_string_4) else 'Not a Palindrome'}")