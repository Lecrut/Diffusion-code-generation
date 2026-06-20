import unicodedata

def count_consonants(text: str) -> int:
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in text:
        if char.isalpha():
            category = unicodedata.category(char)
            if category.startswith('L') and char not in vowels:
                decomposed = unicodedata.normalize('NFD', char)
                if not any(c in vowels for c in decomposed):
                    consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    sample_text = "Hello World! café naïve résumé"
    result = count_consonants(sample_text)
    print(result)