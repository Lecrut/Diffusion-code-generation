import re

def count_consonants(word):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_word = re.sub(pattern, '', word)
    consonant_pattern = r'[^aeiouAEIOU\s\d]'
    consonants = re.findall(consonant_pattern, cleaned_word)
    return len(consonants)

if __name__ == '__main__':
    sample_words = [
        "Hello, World!",
        "Python3.9",
        "Café résumé",
        "12345",
        "!@#$%^&*()",
        "aeiouAEIOU",
        "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ",
        "   spaces   ",
        "",
        "Mixed123!@#Chars"
    ]
    for word in sample_words:
        print(count_consonants(word))