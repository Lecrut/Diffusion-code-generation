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
    sample_text = "This is a test sentence with some words like programming and education."
    result = find_vowel_words(sample_text)
    print(result)