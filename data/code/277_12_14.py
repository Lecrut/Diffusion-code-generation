VOWELS = "aeiou"

def count_vowels(text):
    vowel_count = 0
    for char in text.lower():
        if char in VOWELS:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    result_1 = count_vowels(sample_string_1)
    print(f"The string: '{sample_string_1}' has {result_1} vowels.")
    
    sample_string_2 = "Programming is Fun"
    result_2 = count_vowels(sample_string_2)
    print(f"The string: '{sample_string_2}' has {result_2} vowels.")
    
    sample_string_3 = "AEIOUaeiou"
    result_3 = count_vowels(sample_string_3)
    print(f"The string: '{sample_string_3}' has {result_3} vowels.")