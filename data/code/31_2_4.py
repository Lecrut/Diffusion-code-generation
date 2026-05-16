def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    sample_string1 = "madam"
    sample_string2 = "hello"
    sample_string3 = "racecar"
    result1 = is_palindrome(sample_string1)
    print(f"'{sample_string1}' is a palindrome: {result1}")
    result2 = is_palindrome(sample_string2)
    print(f"'{sample_string2}' is a palindrome: {result2}")
    result3 = is_palindrome(sample_string3)
    print(f"'{sample_string3}' is a palindrome: {result3}")