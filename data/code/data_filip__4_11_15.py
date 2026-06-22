def count_consonants(word: str) -> int:
    vowels = set('aeiouAEIOU')
    return len([char for char in word if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    test_word = "Hello, World!"
    print(count_consonants(test_word))