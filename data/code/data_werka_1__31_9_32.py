def is_palindrome(s):
    return s.lower() == s[::-1].lower()

if __name__ == '__main__':
    sample_values = ["Racecar", "hello", "A man a plan a canal Panama"]
    results = [is_palindrome(value) for value in sample_values]
    print(results)