def count_consonants(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return len([char for char in word if char.isalpha() and char.lower() not in vowels])

if __name__ == '__main__':
    test_words = ["Hello, World!", "Rhythm", "AEIOU", "Python3.9", "bcdfg"]
    for w in test_words:
        print(count_consonants(w))