def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == '__main__':
    sample_input = "A man a plan a canal Panama"
    result = is_palindrome(sample_input)
    print(result)