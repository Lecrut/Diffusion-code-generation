VOWELS = {'a', 'e', 'i', 'o', 'u'}

def identify_vowel_words(text):
    words = text.lower().split()
    return {word for word in words if any(char in VOWELS for char in word)}

if __name__ == '__main__':
    sample_text = "This is a test sentence with many words including apple and banana."
    result = identify_vowel_words(sample_text)
    print(result)