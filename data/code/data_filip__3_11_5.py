VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def strip_vowels(text):
    return ''.join([char for char in text if char not in VOWELS])

if __name__ == '__main__':
    sample_text = "Programming is fun and powerful"
    result = strip_vowels(sample_text)
    print(result)