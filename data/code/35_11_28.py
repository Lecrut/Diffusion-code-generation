def count_vowels(text):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0,
              'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    for char in text:
        if char in vowels:
            vowels[char] += 1
    return sum(vowels.values())

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Python Programming"
    sample_string_3 = "Rhythm"
    sample_string_4 = "AEIOUaeiou123!"
    print(f"'{sample_string_1}': {count_vowels(sample_string_1)}")
    print(f"'{sample_string_2}': {count_vowels(sample_string_2)}")
    print(f"'{sample_string_3}': {count_vowels(sample_string_3)}")
    print(f"'{sample_string_4}': {count_vowels(sample_string_4)}")