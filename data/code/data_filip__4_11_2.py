def count_consonants(word):
    vowels = set('aeiouAEIOU')
    return sum(1 for c in word if c.isalpha() and c not in vowels)

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    print(count_consonants(sample_word))
    print(count_consonants("AEIOU"))
    print(count_consonants("bcdfg"))
    print(count_consonants(""))
    print(count_consonants("Python3.9!"))