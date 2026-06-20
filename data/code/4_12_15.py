import re

def count_consonants(text):
    letters = re.sub(r'[^a-zA-Z]', '', text)
    vowels = re.sub(r'[aeiouAEIOU]', '', letters)
    return len(vowels)

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)