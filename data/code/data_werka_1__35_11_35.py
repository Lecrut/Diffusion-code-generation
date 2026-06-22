def count_vowels(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Python Programming"
    sample_string_3 = "Rhythm"
    sample_string_4 = "AEIOUaeiou123!"
    
    try:
        print(f"'{sample_string_1}': {count_vowels(sample_string_1)}")
        print(f"'{sample_string_2}': {count_vowels(sample_string_2)}")
        print(f"'{sample_string_3}': {count_vowels(sample_string_3)}")
        print(f"'{sample_string_4}': {count_vowels(sample_string_4)}")
    except ValueError as e:
        print(e)