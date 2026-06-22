def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    print(f"The string: '{sample_string_1}' has {count_vowels(sample_string_1)} vowels.")
    
    sample_string_2 = "Programming is Fun"
    print(f"The string: '{sample_string_2}' has {count_vowels(sample_string_2)} vowels.")
    
    sample_string_3 = "AEIOUaeiou"
    print(f"The string: '{sample_string_3}' has {count_vowels(sample_string_3)} vowels.")