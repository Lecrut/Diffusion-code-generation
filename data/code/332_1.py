def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string_1 = "Hello World"
    result_1 = count_vowels(test_string_1)
    print(f"'{test_string_1}': {result_1}")
    test_string_2 = "AEIOUaeiou"
    result_2 = count_vowels(test_string_2)
    print(f"'{test_string_2}': {result_2}")
    test_string_3 = "Rhythm"
    result_3 = count_vowels(test_string_3)
    print(f"'{test_string_3}': {result_3}")
    test_string_4 = ""
    result_4 = count_vowels(test_string_4)
    print(f"'{test_string_4}': {result_4}")