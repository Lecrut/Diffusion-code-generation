import re

def count_consonants(text):
    vowels = set('aeiouAEIOU')
    letters_only = re.findall(r'[a-zA-Z]', text)
    return len([char for char in letters_only if char not in vowels])

if __name__ == '__main__':
    test_string = "Hello, World! 123 This is a TEST string with vowels AEIOU and consonants."
    result = count_consonants(test_string)
    print(result)