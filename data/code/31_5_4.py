def is_palindrome_two_pointers(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
if __name__ == '__main__':
    string1 = "racecar"
    string2 = "hello"
    string3 = "madam"
    string4 = "apple"
    string5 = ""
    string6 = "aabbaa"
    print(f"'{string1}' is palindrome: {is_palindrome_two_pointers(string1)}")
    print(f"'{string2}' is palindrome: {is_palindrome_two_pointers(string2)}")
    print(f"'{string3}' is palindrome: {is_palindrome_two_pointers(string3)}")
    print(f"'{string4}' is palindrome: {is_palindrome_two_pointers(string4)}")
    print(f"'{string5}' is palindrome: {is_palindrome_two_pointers(string5)}")
    print(f"'{string6}' is palindrome: {is_palindrome_two_pointers(string6)}")