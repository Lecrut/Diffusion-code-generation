def count_consonants(word: str) -> int:
    vowels = set('aeiouAEIOU')
    consonant_set = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    count = 0
    for char in word:
        if char in consonant_set and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    word = "Hello World!"
    result = count_consonants(word)
    print(result)