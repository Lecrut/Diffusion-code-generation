VOWELS = frozenset(['a', 'e', 'i', 'o', 'u'])
count_vowels = lambda text: sum(1 for char in text.casefold() if char in VOWELS)
if __name__ == '__main__':
    sample_text = "Cryptographic systems ensure data integrity"
    print(count_vowels(sample_text))
    print(count_vowels("Rhythm"))
    print(count_vowels(""))