VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def remove_vowels(text):
    return ''.join([char for char in text if char not in VOWELS])

if __name__ == '__main__':
    sample_text = "Hello World, this is a test string with AEIOU vowels."
    result = remove_vowels(sample_text)
    print(result)