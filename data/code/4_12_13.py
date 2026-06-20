import re

def count_consonants(text: str) -> int:
    vowels_and_non_letters = re.compile(r'[^bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    return len(vowels_and_non_letters.sub('', text))

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    print(count_consonants(test_string))