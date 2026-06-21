def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return all(s[i] == s[~i] for i in range(len(s) // 2))

if __name__ == '__main__':
    sample_string = "A man a plan a canal Panama"
    print(is_palindrome(sample_string))