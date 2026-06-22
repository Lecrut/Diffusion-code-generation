def is_palindrome(s):
    normalized_str = ''.join((c.lower() for c in s if c.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    sample_values = ['', 'A man, a plan, a canal: Panama', 'racecar', 'hello', '!@#$%^&*()', "No 'x' in Nixon"]
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")