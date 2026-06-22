import re

def count_consonants(text):
    vowels = set("aeiouAEIOU")
    letters = re.findall(r'[a-zA-Z]', text)
    return sum(1 for char in letters if char not in vowels)

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    result = count_consonants(test_string)
    print(result)