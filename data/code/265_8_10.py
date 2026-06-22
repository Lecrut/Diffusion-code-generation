def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def extract_and_reverse_consonants(phrase):
    consonants = [char for char in phrase if not is_vowel(char)]
    return ''.join(consonants[::-1])

if __name__ == '__main__':
    sample_phrase = 'Hello, World!'
    result = extract_and_reverse_consonants(sample_phrase)
    print(result)