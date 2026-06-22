def is_palindrome(s):
    cleaned = ''.join((char.lower() for char in s if char.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_values = ['', 'A man, a plan, a canal: Panama', 'racecar', 'hello', 'Was it a car or a cat I saw?', '!@#$%^&*()', "No 'x' in Nixon"]
    for value in sample_values:
        print(f"'{value}' is palindrome: {is_palindrome(value)}")