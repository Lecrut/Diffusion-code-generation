import re

def is_palindrome(s):
    cleaned_s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return cleaned_s == cleaned_s[::-1]
if __name__ == '__main__':
    test_cases = ['A man, a plan, a canal: Panama', 'racecar', 'hello', "No 'x' in Nixon", '']
    for case in test_cases:
        print(f"'{case}' -> {is_palindrome(case)}")