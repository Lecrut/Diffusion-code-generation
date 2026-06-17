def count_vowels(text):
    vowel_count = 0
    vowels = "aeiou"
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    sample_string = "Hello World! This is a Test."
    result = count_vowels(sample_string)
    print(result)