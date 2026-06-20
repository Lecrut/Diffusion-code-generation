import string

def remove_vowels(s: str) -> str:
    vowels = 'aeiouAEIOU'
    translation_table = str.maketrans('', '', vowels)
    return s.translate(translation_table)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)