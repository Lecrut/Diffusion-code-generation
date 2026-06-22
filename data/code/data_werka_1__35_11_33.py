def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def count_vowels(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return sum(is_vowel(char) for char in text)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Python Programming"
    sample_string_3 = "Rhythm"
    sample_string_4 = "AEIOUaeiou123!"
    
    print(f"'{sample_string_1}': {count_vowels(sample_string_1)}")
    print(f"'{sample_string_2}': {count_vowels(sample_string_2)}")
    print(f"'{sample_string_3}': {count_vowels(sample_string_3)}")
    print(f"'{sample_string_4}': {count_vowels(sample_string_4)}")