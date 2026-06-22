def remove_vowels(text):
    return ''.join(char for char in text if char.lower() not in 'aeiou')

if __name__ == '__main__':
    print(remove_vowels('hello'))
    print(remove_vowels('world'))
    print(remove_vowels('Hello, World!'))
    print(remove_vowels('Python'))
    print(remove_vowels('AEIOUaeiou'))