def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ['racecar', 'hello', 'madam', 'python', 'a', 'abba']
    for value in sample_values:
        print(is_palindrome(value))