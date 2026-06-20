def count_consonants(s):
    vowels = set('aeiouAEIOU')
    consonants = set([c for c in s if c.isalpha() and c not in vowels])
    return len(consonants)

if __name__ == '__main__':
    sample = "Hello World!"
    print(count_consonants(sample))