def count_consonants(word):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in word if char.isalpha() and char not in vowels)

if __name__ == '__main__':
    print(count_consonants("Hello, World!"))
    print(count_consonants("Python"))
    print(count_consonants("12345!@#$%"))
    print(count_consonants(""))
    print(count_consonants("aeiouAEIOU"))
    print(count_consonants("bcdfgBCDFG"))