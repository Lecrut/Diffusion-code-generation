import re

def count_consonants(word):
    cleaned = re.sub(r'[^a-zA-Z]', '', word)
    vowels = set('aeiouAEIOU')
    consonant_count = sum(1 for char in cleaned if char not in vowels)
    return consonant_count

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    result = count_consonants(sample_word)
    print(result)