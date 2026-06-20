vowels = set('aeiou')

def is_vowel(char):
    return char.lower() in vowels

if __name__ == '__main__':
    test_chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'b', 'c']
    for char in test_chars:
        print(f"'{char}' is a vowel: {is_vowel(char)}")