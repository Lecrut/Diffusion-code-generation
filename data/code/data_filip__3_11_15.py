VOWEL_FLAGS = {
    'a': True,
    'e': True,
    'i': True,
    'o': True,
    'u': True,
    'A': True,
    'E': True,
    'I': True,
    'O': True,
    'U': True,
}

def strip_vowels(text):
    return ''.join([char for char in text if not VOWEL_FLAGS.get(char, False)])

if __name__ == '__main__':
    sample_text = "Programming is fun and educational"
    result = strip_vowels(sample_text)
    print(result)