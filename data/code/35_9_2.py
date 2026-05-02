def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_string_one = "Hello World"
    sample_string_two = "Programming is fun"
    sample_string_three = "AEIOUaeiou"
    sample_string_four = "Rhythm"
    count_one = count_vowels(sample_string_one)
    count_two = count_vowels(sample_string_two)
    count_three = count_vowels(sample_string_three)
    count_four = count_vowels(sample_string_four)
    print(f"'{sample_string_one}' has {count_one} vowels.")
    print(f"'{sample_string_two}' has {count_two} vowels.")
    print(f"'{sample_string_three}' has {count_three} vowels.")
    print(f"'{sample_string_four}' has {count_four} vowels.")