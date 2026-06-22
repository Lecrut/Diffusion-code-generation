import re

def count_consonants(text):
    consonants_only = re.sub('[^bcdfghjklmnpqrstvwxyz]', '', text.lower())
    return len(consonants_only)
if __name__ == '__main__':
    sample_text = 'Hello, World! This is a test string with 123 numbers and @#$ special characters.'
    result = count_consonants(sample_text)
    print(result)