VOWELS = {'a', 'e', 'i', 'o', 'u'}

def contains_vowel(word):
    return any(char in VOWELS for char in word.lower())

def find_vowel_words(text):
    words = text.split()
    vowel_words = [word for word in words if contains_vowel(word)]
    return vowel_words

if __name__ == '__main__':
    sample_text = "This is a test sentence with many vowels and consonants. Programming is fun."
    result = find_vowel_words(sample_text)
    print(result)