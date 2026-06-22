VOWELS = 'aeiouAEIOU'

def extract_consonants_reverse(phrase):
    consonants = [char for char in phrase if char not in VOWELS]
    return ''.join(consonants[::-1])

if __name__ == '__main__':
    sample_phrase = 'Hello, World!'
    result = extract_consonants_reverse(sample_phrase)
    print(result)