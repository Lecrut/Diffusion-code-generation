import string
def count_vowels(text):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    sample_string = "Programming is an interesting task"
    result = count_vowels(sample_string)
    print(result)