import unicodedata

def count_consonants(text: str) -> int:
    if not text:
        return 0
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char not in vowels:
                consonant_count += 1
    return consonant_count
if __name__ == '__main__':
    sample_text = 'Héllo Wörld! This is a test with üñîcödé and Cönsönànts.'
    result = count_consonants(sample_text)
    print(result)