VOWELS = 'aeiouAEIOU'

def extract_vowels_reverse(phrase):
    vowels_found = [char for char in phrase if char in VOWELS]
    return ''.join(vowels_found[::-1])
if __name__ == '__main__':
    sample_phrase = 'Hello World!'
    result = extract_vowels_reverse(sample_phrase)
    print(result)