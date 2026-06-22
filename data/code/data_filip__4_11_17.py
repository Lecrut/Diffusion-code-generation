def count_consonants(word: str) -> int:
    vowels = set('aeiouAEIOU')
    return len([char for char in word if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    print(count_consonants(sample_word))