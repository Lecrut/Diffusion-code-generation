def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    test_string1 = "madam"
    test_string2 = "hello"
    test_string3 = "racecar"
    test_string4 = "A man a plan a canal Panama"
    print(f"Testing '{test_string1}': {is_palindrome(test_string1)}")
    print(f"Testing '{test_string2}': {is_palindrome(test_string2)}")
    print(f"Testing '{test_string3}': {is_palindrome(test_string3)}")
    print(f"Testing '{test_string4}': {is_palindrome(test_string4)}")