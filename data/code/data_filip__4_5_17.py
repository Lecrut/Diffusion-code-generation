def count_consonants(word):
    vowels = 'aeiouAEIOU'
    filtered = list(filter(lambda char: char.isalpha() and char not in vowels, word))
    return len(filtered)

if __name__ == '__main__':
    sample_word = 'Python'
    result = count_consonants(sample_word)
    print(result)