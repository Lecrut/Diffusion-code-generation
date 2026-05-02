import string
def count_vowels_single_pass(text):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    sample_string = "This is a long string with many vowels"
    result = count_vowels_single_pass(sample_string)
    print(result)