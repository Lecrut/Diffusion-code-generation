def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonant_count = len(filter(lambda c: c.isalpha() and c not in vowels, word))
    return consonant_count

if __name__ == '__main__':
    word = 'Python'
    result = count_consonants(word)
    print(result)