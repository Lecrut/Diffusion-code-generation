def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_text = "madam"
    result = is_palindrome(sample_text)
    print(result)