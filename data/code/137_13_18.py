def is_vowel(char):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return char.lower() in vowels

if __name__ == '__main__':
    test_chars = ['A', 'e', 'I', 'O', 'U', 'b', 'c']
    for char in test_chars:
        print(f"'{char}' is a vowel: {is_vowel(char)}")