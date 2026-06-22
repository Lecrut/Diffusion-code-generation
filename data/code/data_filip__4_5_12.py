def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonants = filter(lambda c: c.isalpha() and c not in vowels, word)
    return len(list(consonants))

if __name__ == '__main__':
    word = "Hello"
    print(count_consonants(word))