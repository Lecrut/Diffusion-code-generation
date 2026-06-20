def filter_vowels(text):
    return ''.join(char for char in text if char.lower() not in 'aeiou')

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string with vowels."
    result = filter_vowels(sample_text)
    print(result)