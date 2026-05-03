import sys
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    sample_string = "racecar"
    result = is_palindrome(sample_string)
    print(f"The string is: {sample_string}")
    print(f"Is it a palindrome? {result}")
    sample_string_2 = "hello"
    result_2 = is_palindrome(sample_string_2)
    print(f"The string is: {sample_string_2}")
    print(f"Is it a palindrome? {result_2}")
    sample_string_3 = "Madam"
    result_3 = is_palindrome(sample_string_3)
    print(f"The string is: {sample_string_3}")
    print(f"Is it a palindrome? {result_3}")