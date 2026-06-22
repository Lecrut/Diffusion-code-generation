import re

def remove_vowels(text):
    vowel_re = re.compile('[aeiouAEIOU]')
    return vowel_re.sub('', text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(remove_vowels(sample_text))