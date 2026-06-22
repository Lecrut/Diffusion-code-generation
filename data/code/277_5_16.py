VOWELS = "aeiouAEIOU"

def count_non_vowels(input_string):
    count = 0
    for char in input_string:
        if char not in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    non_vowel_count = count_non_vowels(sample_string)
    print(f"Number of non-vowel characters in '{sample_string}': {non_vowel_count}")