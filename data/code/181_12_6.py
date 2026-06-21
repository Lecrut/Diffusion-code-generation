def isolate_vowel_words(text):
    vowels = 'aeiouAEIOU'
    return [word for word in text.split() if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_text = "Hello world, this is a test."
    print(isolate_vowel_words(sample_text))