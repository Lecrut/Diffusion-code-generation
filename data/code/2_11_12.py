def is_palindrome(text):
    return text == text[::-1]
if __name__ == '__main__':
    sample_values = ['racecar', 'hello', 'madam', 'python', 'a', '', 'abba', 'abcba']
    for value in sample_values:
        result = is_palindrome(value)
        print(f"is_palindrome('{value}') = {result}")