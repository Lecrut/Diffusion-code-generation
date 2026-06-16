def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Python Programming"
    test_string_3 = ""
    test_string_4 = "AEIOUaeiou"
    result_1 = count_vowels(test_string_1)
    result_2 = count_vowels(test_string_2)
    result_3 = count_vowels(test_string_3)
    result_4 = count_vowels(test_string_4)
    print(f"'{test_string_1}': {result_1}")
    print(f"'{test_string_2}': {result_2}")
    print(f"'{test_string_3}': {result_3}")
    print(f"'{test_string_4}': {result_4}")