def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def count_non_vowels(input_string):
    non_vowel_count = 0
    for char in input_string:
        if not is_vowel(char):
            non_vowel_count += 1
    return non_vowel_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_non_vowels(sample_string)
    print(f"Number of non-vowel characters in '{sample_string}': {result}")