VOWEL_MAP = {c: False for c in 'aeiouAEIOU'}

def remove_vowels(text):
    return ''.join([char for char in text if VOWEL_MAP.get(char, True)])

if __name__ == '__main__':
    sample_input = "Python Programming"
    output = remove_vowels(sample_input)
    print(output)