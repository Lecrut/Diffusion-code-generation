VOWEL_MAP = {
    'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
    'A': True, 'E': True, 'I': True, 'O': True, 'U': True
}

def delete_vowels(text):
    return "".join(char for char in text if not VOWEL_MAP.get(char, False))

if __name__ == '__main__':
    sample_input = "The Quick Brown Fox Jumps Over The Lazy Dog"
    output_text = delete_vowels(sample_input)
    print(output_text)