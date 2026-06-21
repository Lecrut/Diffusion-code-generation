import re

def count_vowels(text):
    vowels = re.findall(r'[aeiouAEIOU]', text)
    return len(vowels)

if __name__ == '__main__':
    test_string = "Hello World, how are you today?"
    print(count_vowels(test_string))