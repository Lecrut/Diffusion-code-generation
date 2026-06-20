def count_consonants(word):
    vowels = set('aeiouAEIOU')
    return len(list(filter(lambda c: c.isalpha() and c not in vowels, word)))

if __name__ == '__main__':
    sample_word = "Programming"
    result = count_consonants(sample_word)
    print(result)