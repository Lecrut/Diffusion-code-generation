import string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_string = "Hello World, this is a test string."
    vowel_count = count_vowels(sample_string)
    print(vowel_count)