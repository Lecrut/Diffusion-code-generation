def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    sample_strings = ["A man a plan a canal Panama", "racecar", "hello"]
    for string in sample_strings:
        print(is_palindrome(string))