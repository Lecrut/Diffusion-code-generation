def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
if __name__ == '__main__':
    sample_string1 = "Hello World"
    sample_string2 = "Python Programming"
    sample_string3 = "AEIOUaeiou"
    print(f"'{sample_string1}': {count_vowels(sample_string1)}")
    print(f"'{sample_string2}': {count_vowels(sample_string2)}")
    print(f"'{sample_string3}': {count_vowels(sample_string3)}")