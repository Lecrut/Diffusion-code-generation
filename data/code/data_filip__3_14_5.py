import re

_vowel_remover = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text: str) -> str:
    return _vowel_remover.sub('', text)

if __name__ == '__main__':
    sample_inputs = ['Hello World', 'AEIOU', 'Rhythm', 'Python Programming']
    for sample in sample_inputs:
        print(remove_vowels(sample))