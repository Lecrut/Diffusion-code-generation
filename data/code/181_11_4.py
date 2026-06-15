import re
def find_vowel_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    vowel_words = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for word in words:
        if any(char in vowels for char in word):
            vowel_words.append(word)
    return vowel_words
if __name__ == '__main__':
    sample_string = "This is a test sentence with many words and some consonants like r, t, c, s."
    result = find_vowel_words(sample_string)
    print(result)