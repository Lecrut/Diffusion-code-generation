def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def count_vowels(text):
    return sum(1 for char in text if is_vowel(char))

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Python Programming"
    sample_string_3 = "Rhythm"
    sample_string_4 = "AEIOUaeiou123!"
    
    print(f"'{sample_string_1}': {count_vowels(sample_string_1)}")
    print(f"'{sample_string_2}': {count_vowels(sample_string_2)}")
    print(f"'{sample_string_3}': {count_vowels(sample_string_3)}")
    print(f"'{sample_string_4}': {count_vowels(sample_string_4)}")