def count_consonants(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    print(count_consonants("Hello, World!"))
    print(count_consonants("Python Programming"))
    print(count_consonants("12345!@#$%"))
    print(count_consonants("AEIOU"))
    print(count_consonants("bcdfg"))