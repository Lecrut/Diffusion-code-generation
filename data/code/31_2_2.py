def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    test_string1 = "racecar"
    test_string2 = "hello"
    test_string3 = "madam"
    test_string4 = "A man a plan a canal Panama"
    print(f"Testing '{test_string1}': {'Palindrome' if is_palindrome(test_string1) else 'Not a Palindrome'}")
    print(f"Testing '{test_string2}': {'Palindrome' if is_palindrome(test_string2) else 'Not a Palindrome'}")
    print(f"Testing '{test_string3}': {'Palindrome' if is_palindrome(test_string3) else 'Not a Palindrome'}")
    print(f"Testing '{test_string4}': {'Palindrome' if is_palindrome(test_string4) else 'Not a Palindrome'}")