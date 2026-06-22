def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "A man a plan a canal Panama", "12321", "Python"]
    for value in sample_values:
        print(is_palindrome(value))