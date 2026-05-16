def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_string1 = "Hello World"
    sample_string2 = "Python Programming"
    sample_string3 = "Rhythm"
    sample_string4 = "AEIOUaeiou123!"
    print(f"'{sample_string1}': {count_vowels(sample_string1)}")
    print(f"'{sample_string2}': {count_vowels(sample_string2)}")
    print(f"'{sample_string3}': {count_vowels(sample_string3)}")
    print(f"'{sample_string4}': {count_vowels(sample_string4)}")