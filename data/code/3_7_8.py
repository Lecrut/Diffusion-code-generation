VOWELS = set('aeiouAEIOU')

def remove_vowels(text):
    return ''.join([char for char in text if char not in VOWELS])

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)