def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_input = "racecar"
    result = is_palindrome(sample_input)
    print(f"The string '{sample_input}' is a palindrome: {result}")