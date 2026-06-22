def count_consonants(word):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in word:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Hello"
    result = count_consonants(sample_word)
    print(result)