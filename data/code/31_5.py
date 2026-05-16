def is_palindrome(s):
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
    string5 = "aabbaa"
    print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
    print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
    print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")
    print(f"'{string4}' is a palindrome: {is_palindrome(string4)}")
    print(f"'{string5}' is a palindrome: {is_palindrome(string5)}")