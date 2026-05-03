import string
def count_vowels(s):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    test_string = "Programming is an efficient algorithm"
    result = count_vowels(test_string)
    print(result)