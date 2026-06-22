def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    print(count_vowels("Hello World"))
    print(count_vowels("AEIOU"))
    print(count_vowels("bcdfg"))
    print(count_vowels(""))
    print(count_vowels("12345!@#"))
    print(count_vowels("Python Programming"))