def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Programming is Fun"
    test_string_3 = "AEIOUaeiou"
    print(f"'{test_string_1}': {count_vowels(test_string_1)}")
    print(f"'{test_string_2}': {count_vowels(test_string_2)}")
    print(f"'{test_string_3}': {count_vowels(test_string_3)}")