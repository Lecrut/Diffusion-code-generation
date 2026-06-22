def strip_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample_text = "Hello World"
    result = strip_vowels(sample_text)
    print(result)