def count_consonants(s: str) -> int:
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return sum(1 for c in s if c in consonants)

if __name__ == '__main__':
    print(count_consonants("Hello, World!"))
    print(count_consonants("Python3.9"))
    print(count_consonants("AEIOU"))
    print(count_consonants(""))
    print(count_consonants("12345!@#$%"))