def count_consonants(word):
    vowels = set("aeiouAEIOU")
    return len(list(filter(lambda char: char.isalpha() and char not in vowels, word)))

if __name__ == "__main__":
    sample_word = "HelloWorld"
    print(count_consonants(sample_word))