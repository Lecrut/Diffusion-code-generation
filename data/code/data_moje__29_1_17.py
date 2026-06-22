count_vowels = lambda text: sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    print(count_vowels('Hello World'))
    print(count_vowels('Python Programming'))
    print(count_vowels('AEIOU'))
    print(count_vowels('bcdfg'))
    print(count_vowels('The quick brown fox jumps over the lazy dog'))