def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
    return consonant_count

def count_consonants_with_filter(word):
    vowels = set('aeiouAEIOU')
    consonants = filter(lambda char: char.isalpha() and char not in vowels, word)
    return sum(1 for _ in consonants)

if __name__ == '__main__':
    word = "HelloWorld"
    result = count_consonants_with_filter(word)
    print(result)