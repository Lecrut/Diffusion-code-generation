def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonants = sum(1 for char in word if char.isalpha() and char not in vowels)
    return consonants

if __name__ == '__main__':
    print(count_consonants("Hello, World!"))
    print(count_consonants("Python3.9"))
    print(count_consonants("AEIOU"))
    print(count_consonants("bcdfg"))
    print(count_consonants("12345!@#$%"))
    print(count_consonants("Rhythm"))