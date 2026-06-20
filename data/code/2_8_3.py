import re

def is_palindrome(text):
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    examples = ["A man, a plan, a canal: Panama", "Race car!", "Hello World"]
    for example in examples:
        print(is_palindrome(example))