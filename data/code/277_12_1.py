def count_vowels(text):
    vowel_count = 0
    vowels = "aeiou"
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    sample_string = "Hello World"
    result = count_vowels(sample_string)
    print(f"The string is: '{sample_string}'")
    print(f"The number of vowels is: {result}")
    sample_string_2 = "Programming is Fun"
    result_2 = count_vowels(sample_string_2)
    print(f"The string is: '{sample_string_2}'")
    print(f"The number of vowels is: {result_2}")