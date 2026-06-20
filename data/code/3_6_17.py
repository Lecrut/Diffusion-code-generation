def remove_vowels(text):
    return ''.join(filter(lambda c: c.lower() not in 'aeiou', text))

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOU aeiou"))