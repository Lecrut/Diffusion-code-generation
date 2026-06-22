import re

def is_palindrome(s):
    cleaned = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    print(is_palindrome('A man, a plan, a canal: Panama'))
    print(is_palindrome('race a car'))