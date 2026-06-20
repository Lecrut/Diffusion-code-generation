def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "Was it a car or a cat I saw?"]
    for s in sample_strings:
        print(is_palindrome(s))