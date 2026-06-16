def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string_1 = "Hello World"
    result_1 = count_vowels(test_string_1)
    print(f"'{test_string_1}' has {result_1} vowels")
    test_string_2 = "Programming is Fun"
    result_2 = count_vowels(test_string_2)
    print(f"'{test_string_2}' has {result_2} vowels")
    test_string_3 = "AEIOUaeiou"
    result_3 = count_vowels(test_string_3)
    print(f"'{test_string_3}' has {result_3} vowels")
    test_string_4 = "Rhythm"
    result_4 = count_vowels(test_string_4)
    print(f"'{test_string_4}' has {result_4} vowels")