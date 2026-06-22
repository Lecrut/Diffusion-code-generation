def count_consonants(input_string):
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in input_string:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count
if __name__ == '__main__':
    sample_input = 'Hello, World!'
    result = count_consonants(sample_input)
    print(result)