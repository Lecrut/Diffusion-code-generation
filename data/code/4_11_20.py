def count_consonants(word):
    vowels = set('aeiouAEIOU')
    return len([char for char in word if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    result = count_consonants(sample_word)
    print(result)