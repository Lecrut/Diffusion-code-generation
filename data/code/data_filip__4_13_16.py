def count_consonants(s):
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    print(count_consonants(sample_string))