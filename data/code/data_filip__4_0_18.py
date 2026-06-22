def count_consonants(s):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return sum(1 for c in s if c in consonants)

if __name__ == '__main__':
    print(count_consonants("Hello, World!"))
    print(count_consonants("Python Programming"))
    print(count_consonants("aeiou"))
    print(count_consonants("12345!@#$%"))
    print(count_consonants("Bcdfghjklmnpqrstvwxyz"))