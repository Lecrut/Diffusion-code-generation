def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Programming is Fun"
    sample_string_3 = "AEIOUaeiou"
    sample_string_4 = "Rhythm"
    count1 = count_vowels(sample_string_1)
    count2 = count_vowels(sample_string_2)
    count3 = count_vowels(sample_string_3)
    count4 = count_vowels(sample_string_4)
    print(f"'{sample_string_1}': {count1}")
    print(f"'{sample_string_2}': {count2}")
    print(f"'{sample_string_3}': {count3}")
    print(f"'{sample_string_4}': {count4}")