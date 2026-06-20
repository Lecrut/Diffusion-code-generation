def count_consonants(text: str) -> int:
    vowels = set('aeiouAEIOU')
    consonant_set = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = 0
    for char in text:
        if char in consonant_set and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)