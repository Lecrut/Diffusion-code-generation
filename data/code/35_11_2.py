def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Python Programming"
    test_string_3 = "Rhythm"
    test_string_4 = "AEIOUaeiou123!"
    print(f"'{test_string_1}': {count_vowels(test_string_1)}")
    print(f"'{test_string_2}': {count_vowels(test_string_2)}")
    print(f"'{test_string_3}': {count_vowels(test_string_3)}")
    print(f"'{test_string_4}': {count_vowels(test_string_4)}")