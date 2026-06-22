VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def strip_vowels(text):
    return ''.join([char for char in text if char not in VOWELS])

if __name__ == '__main__':
    sample_input = "Hello World, this is a Python Script!"
    result = strip_vowels(sample_input)
    print(result)