def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    print(count_consonants("Hello World"))
    print(count_consonants("Python Programming"))
    print(count_consonants("AEIOU aeiou"))
    print(count_consonants("12345!@#$%"))
    print(count_consonants("Bjork"))