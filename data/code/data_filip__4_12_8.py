import re

def count_consonants(text):
    vowels_and_non_letters = re.compile(r'[^bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', re.IGNORECASE)
    consonants_only = vowels_and_non_letters.sub('', text)
    return len(consonants_only)

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    print(count_consonants(test_string))