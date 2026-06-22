VOWEL_SET = frozenset('aeiouAEIOU')

def strip_vowels(text):
    consonants = [character for character in text if character not in VOWEL_SET]
    return ''.join(consonants)

if __name__ == '__main__':
    sample_string = "Beautiful Day"
    cleaned_text = strip_vowels(sample_string)
    print(cleaned_text)