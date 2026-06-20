import unicodedata

def count_consonants(text: str) -> int:
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

def is_vowel(char: str) -> bool:
    vowels = set("aeiouAEIOU")
    return char in vowels

def is_consonant(char: str) -> bool:
    return char.isalpha() and not is_vowel(char)

if __name__ == '__main__':
    sample_text = "Hello, World! Привет мир. Cönsonants: ß, ʒ, ʃ, ʔ"
    result = count_consonants(sample_text)
    print(result)