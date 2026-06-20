def remove_vowels(text):
    return ''.join(char for char in text if char.lower() not in 'aeiou')

if __name__ == '__main__':
    sample_text = "Hello World"
    print(remove_vowels(sample_text))
    sample_text2 = "Python Programming"
    print(remove_vowels(sample_text2))
    sample_text3 = "AEIOU aeiou"
    print(remove_vowels(sample_text3))