import unicodedata

def count_consonants(text):
    normalized_text = unicodedata.normalize('NFKC', text)
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in normalized_text:
        if char.isalpha():
            if char not in vowels:
                consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    sample_string = "Hello, World! ¡Café 123 Ñoño π∑"
    result = count_consonants(sample_string)
    print(result)