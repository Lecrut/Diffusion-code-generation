def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string1 = "Hello World"
    test_string2 = "Programming is Fun"
    test_string3 = "AEIOUaeiou"
    test_string4 = "Rhythm"
    print(f"'{test_string1}': {count_vowels(test_string1)}")
    print(f"'{test_string2}': {count_vowels(test_string2)}")
    print(f"'{test_string3}': {count_vowels(test_string3)}")
    print(f"'{test_string4}': {count_vowels(test_string4)}")