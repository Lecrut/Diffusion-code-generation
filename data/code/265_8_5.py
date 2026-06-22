def extract_reverse_consonants(phrase):
    vowels = "aeiouAEIOU"
    consonants = [char for char in phrase if char not in vowels]
    return ''.join(consonants[::-1])

if __name__ == '__main__':
    sample_phrase = "Hello World"
    print(extract_reverse_consonants(sample_phrase))