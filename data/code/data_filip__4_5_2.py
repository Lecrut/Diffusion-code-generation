def count_consonants(word):
    vowels = set("aeiouAEIOU")
    consonant_filter = lambda char: char.isalpha() and char not in vowels
    consonants = filter(consonant_filter, word)
    return len(list(consonants))

if __name__ == '__main__':
    word = "HelloWorld"
    result = count_consonants(word)
    print(result)