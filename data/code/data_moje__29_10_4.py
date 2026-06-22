def count_vowels(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "AEIOUaeiou"
    sample_string_3 = "Rhythm myths"
    print(count_vowels(sample_string_1))
    print(count_vowels(sample_string_2))
    print(count_vowels(sample_string_3))