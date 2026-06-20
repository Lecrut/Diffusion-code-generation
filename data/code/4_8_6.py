def count_consonants(input_string):
    vowels = set('aeiouAEIOU')
    consonants_count = 0
    for char in input_string:
        if char.isalpha() and char not in vowels:
            consonants_count += 1
    return consonants_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_consonants(sample_string)
    print(result)