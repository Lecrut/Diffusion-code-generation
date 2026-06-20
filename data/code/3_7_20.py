def remove_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample_text = "Hello, World! Programming is fun."
    result = remove_vowels(sample_text)
    print(result)