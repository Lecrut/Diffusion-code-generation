def isolate_vowel_words(text):
    words = text.split()
    vowel_words = [word for word in words if any(char.lower() in 'aeiou' for char in word)]
    return vowel_words

if __name__ == '__main__':
    sample_text = "Hello world, this is a test of the emergency broadcast system."
    print(isolate_vowel_words(sample_text))