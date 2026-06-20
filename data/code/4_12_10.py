import re

def count_consonants(text):
    consonant_pattern = '[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
    consonants = re.findall(consonant_pattern, text)
    return len(consonants)
if __name__ == '__main__':
    test_string = 'Hello World! This is a test string with 123 numbers and @# symbols.'
    result = count_consonants(test_string)
    print(result)