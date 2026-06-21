def count_vowels(text):
    unique_chars = set(text.lower())
    vowels = set('aeiou')
    unique_vowels = unique_chars.intersection(vowels)
    return len(unique_vowels)

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = count_vowels(sample_text)
    print(result)