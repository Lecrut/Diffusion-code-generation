def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_string = "racecar"
    print(is_palindrome(sample_string))