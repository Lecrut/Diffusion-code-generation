def count_consonants(word):
    vowels = set("aeiouAEIOU")
    consonants = filter(lambda char: char.isalpha() and char not in vowels, word)
    return sum(1 for _ in consonants)

if __name__ == '__main__':
    word = "HelloWorld"
    result = count_consonants(word)
    print(result)