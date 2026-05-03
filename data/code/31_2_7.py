def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    sample_string1 = "madam"
    sample_string2 = "hello"
    sample_string3 = "racecar"
    print(f"Checking '{sample_string1}': {'Palindrome' if is_palindrome(sample_string1) else 'Not a Palindrome'}")
    print(f"Checking '{sample_string2}': {'Palindrome' if is_palindrome(sample_string2) else 'Not a Palindrome'}")
    print(f"Checking '{sample_string3}': {'Palindrome' if is_palindrome(sample_string3) else 'Not a Palindrome'}")