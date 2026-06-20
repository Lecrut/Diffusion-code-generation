def count_consonants(word):
    vowels = "aeiouAEIOU"
    consonants = list(filter(lambda char: char.isalpha() and char not in vowels, word))
    return len(consonants)

if __name__ == '__main__':
    sample_word = "Programming"
    result = count_consonants(sample_word)
    print(result)