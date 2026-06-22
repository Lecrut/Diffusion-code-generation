def count_non_vowels(input_string):
    vowels = "aeiouAEIOU"
    non_vowel_count = 0
    for char in input_string:
        if char not in vowels:
            non_vowel_count += 1
    return non_vowel_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_non_vowels(sample_string)
    print(f"Number of non-vowel characters in '{sample_string}': {result}")