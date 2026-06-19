def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join((char for char in s if char.isalnum()))
    return s == s[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal: Panama', 'racecar', 'hello', "No 'x' in Nixon"]
    for value in sample_values:
        print(is_palindrome(value))