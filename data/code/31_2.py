def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    sample_string1 = "racecar"
    sample_string2 = "hello"
    sample_string3 = "madam"
    result1 = is_palindrome(sample_string1)
    print(f"Input: {sample_string1}")
    print(f"Is palindrome: {result1}")
    result2 = is_palindrome(sample_string2)
    print(f"Input: {sample_string2}")
    print(f"Is palindrome: {result2}")
    result3 = is_palindrome(sample_string3)
    print(f"Input: {sample_string3}")
    print(f"Is palindrome: {result3}")