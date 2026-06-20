def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonants = [c for c in word if c.isalpha() and c not in vowels]
    return len(consonants)

if __name__ == '__main__':
    word = "Hello"
    result = count_consonants(word)
    print(result)