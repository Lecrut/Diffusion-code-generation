def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Programming is fun"
    sample_string_3 = "AEIOUaeiou"
    print(count_vowels(sample_string_1))
    print(count_vowels(sample_string_2))
    print(count_vowels(sample_string_3))