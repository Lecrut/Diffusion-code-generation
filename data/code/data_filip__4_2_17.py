def count_consonants(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_count = 0
    for char in s:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in vowels:
                consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    result = count_consonants(test_string)
    print(result)