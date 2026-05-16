import sys
def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string_1 = "Hello World"
    result_1 = count_vowels(test_string_1)
    print(result_1)
    test_string_2 = "Programming is Fun"
    result_2 = count_vowels(test_string_2)
    print(result_2)
    test_string_3 = "AEIOUaeiou"
    result_3 = count_vowels(test_string_3)
    print(result_3)