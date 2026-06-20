def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    print(remove_vowels('Hello World'))
    print(remove_vowels('Python Programming'))
    print(remove_vowels('AEIOU aeiou'))
    print(remove_vowels('bcdfg'))