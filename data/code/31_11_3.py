import sys
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    sample_string = "Racecar"
    result = is_palindrome(sample_string)
    print(f"The string entered is: {sample_string}")
    print(f"Is the string a palindrome? {result}")