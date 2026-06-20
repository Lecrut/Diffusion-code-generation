import re

def count_consonants(text):
    consonants_pattern = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    matches = consonants_pattern.findall(text)
    return len(matches)

if __name__ == '__main__':
    sample_word = "Hello, World! 123 @#$"
    result = count_consonants(sample_word)
    print(result)