def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
if __name__ == '__main__':
    test_string1 = "Hello World"
    test_string2 = "Python Programming"
    test_string3 = "Rhythm"
    print(f"'{test_string1}': {count_vowels(test_string1)}")
    print(f"'{test_string2}': {count_vowels(test_string2)}")
    print(f"'{test_string3}': {count_vowels(test_string3)}")