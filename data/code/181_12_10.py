def isolate_words_with_vowels(text):
    vowels = 'aeiouAEIOU'
    return [word for word in text.split() if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    print(isolate_words_with_vowels(sample_text))