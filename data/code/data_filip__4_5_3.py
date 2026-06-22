def count_consonants(word):
    vowels = 'aeiouAEIOU'
    consonant_list = filter(lambda char: char.isalpha() and char not in vowels, word)
    return len(list(consonant_list))

if __name__ == '__main__':
    sample_word = 'Programming'
    result = count_consonants(sample_word)
    print(result)