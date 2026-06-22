def count_vowels(text):
    vowel_count = 0
    vowels = "aeiou"
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_string_1 = "Python Programming"
    result_1 = count_vowels(sample_string_1)
    print(f"The string: '{sample_string_1}' has {result_1} vowels.")
    
    sample_string_2 = "Data Science is Cool!"
    result_2 = count_vowels(sample_string_2)
    print(f"The string: '{sample_string_2}' has {result_2} vowels.")