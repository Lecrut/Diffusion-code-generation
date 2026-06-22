def count_consonants(word):
    vowels = 'aeiouAEIOU'
    return len(list(filter(lambda char: char.isalpha() and char not in vowels, word)))

if __name__ == '__main__':
    sample_word = "Python"
    result = count_consonants(sample_word)
    print(result)