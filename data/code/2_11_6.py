def is_palindrome(s: str) -> bool:
    return s == s[::-1]
if __name__ == '__main__':
    sample_strings = ['radar', 'hello', 'A man a plan a canal Panama', 'Was it a car or a cat I saw?', '', 'a', 'ab']
    for test_string in sample_strings:
        result = is_palindrome(test_string.lower().replace(' ', '').replace(',', '').replace('?', ''))
        print(f"'{test_string}' -> {result}")