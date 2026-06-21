VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def contains_vowel(s: str) -> bool:
    return any(char in VOWELS for char in s)

if __name__ == '__main__':
    test_string_1 = "hello"
    test_string_2 = "rhythm"
    test_string_3 = "aeiou"
    test_string_4 = ""
    test_string_5 = "Bcdfghjkl"
    print(f"'{test_string_1}' contains a vowel: {contains_vowel(test_string_1)}")
    print(f"'{test_string_2}' contains a vowel: {contains_vowel(test_string_2)}")
    print(f"'{test_string_3}' contains a vowel: {contains_vowel(test_string_3)}")
    print(f"'{test_string_4}' contains a vowel: {contains_vowel(test_string_4)}")
    print(f"'{test_string_5}' contains a vowel: {contains_vowel(test_string_5)}")