def is_palindrome(s):
    normalized_str = ''.join((char.lower() for char in s if char.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    sample_values = ['', 'A man, a plan, a canal: Panama', 'racecar', 'hello', 'Was it a car or a cat I saw?', "No 'x' in Nixon", '12321', '123456']
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")