import re

def count_consonants(word):
    if not isinstance(word, str):
        raise TypeError('Input must be a string')
    consonant_pattern = '[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
    matches = re.findall(consonant_pattern, word)
    return len(matches)
if __name__ == '__main__':
    test_words = ['hello', 'world', 'aeiou', 'bcdfg', 'Hello World', 'Python3.9', 'Special!@#Characters$%', '', '12345', 'rhythm', 'fly', 'queue', 'strengths', 'grrr', 'a']
    for test_word in test_words:
        consonant_count = count_consonants(test_word)
        print(f"Word: '{test_word}' -> Consonants: {consonant_count}")