def count_consonants(word):
    vowels = "aeiouAEIOU"
    return len(list(filter(lambda c: c.isalpha() and c not in vowels, word)))

if __name__ == "__main__":
    sample_word = "Python"
    print(count_consonants(sample_word))