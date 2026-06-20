def check_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

if __name__ == '__main__':
    sample_string = "racecar"
    result = check_palindrome(sample_string)
    print(result)