def count_vowels(text):
    vowel_count = 0
    vowels = "aeiou"
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    sample_string_1 = "Hello World"
    result_1 = count_vowels(sample_string_1)
    print(f"The number of vowels in '{sample_string_1}' is: {result_1}")
    sample_string_2 = "Programming is Fun"
    result_2 = count_vowels(sample_string_2)
    print(f"The number of vowels in '{sample_string_2}' is: {result_2}")
    sample_string_3 = "AEIOUaeiou"
    result_3 = count_vowels(sample_string_3)
    print(f"The number of vowels in '{sample_string_3}' is: {result_3}")