def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    sample_string1 = "racecar"
    sample_string2 = "hello"
    sample_string3 = "madam"
    print(f"Checking '{sample_string1}': {is_palindrome(sample_string1)}")
    print(f"Checking '{sample_string2}': {is_palindrome(sample_string2)}")
    print(f"Checking '{sample_string3}': {is_palindrome(sample_string3)}")