def count_consonants(word):
    vowels = set('aeiouAEIOU')
    return len([char for char in word if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    test_words = ["Hello", "Python3", "123", "Sky", "aEiOu"]
    results = []
    for w in test_words:
        results.append(count_consonants(w))
    print(results)