def isolate_vowel_words(text):
    return [word for word in text.split() if any(vowel in word.lower() for vowel in 'aeiou')]

if __name__ == '__main__':
    sample_text = "Hello world, this is a test."
    print(isolate_vowel_words(sample_text))