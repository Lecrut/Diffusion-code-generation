import re

def count_consonants(word):
    consonant_pattern = re.compile('[bcdfghjklmnpqrstvwxyz]', re.IGNORECASE)
    matches = consonant_pattern.findall(word)
    return len(matches)
if __name__ == '__main__':
    test_words = ['Hello', 'World', 'Rhythm', 'AEIOU', 'BCDFG', '12345!@#$%', '', 'Python3.9', 'Fly', 'Queue']
    for word in test_words:
        result = count_consonants(word)
        print(f"Word: '{word}' -> Consonant count: {result}")