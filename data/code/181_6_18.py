def contains_vowel(s: str) -> bool:
    vowels = set('aeiouAEIOU')
    return any(char in vowels for char in s)

if __name__ == '__main__':
    test_string_1 = "example"
    test_string_2 = "sky"
    test_string_3 = "encyclopedia"
    test_string_4 = ""
    test_string_5 = "BCDFGHJKLMNPQRSTVWXYZ"
    
    print(f"'{test_string_1}' contains a vowel: {contains_vowel(test_string_1)}")
    print(f"'{test_string_2}' contains a vowel: {contains_vowel(test_string_2)}")
    print(f"'{test_string_3}' contains a vowel: {contains_vowel(test_string_3)}")
    print(f"'{test_string_4}' contains a vowel: {contains_vowel(test_string_4)}")
    print(f"'{test_string_5}' contains a vowel: {contains_vowel(test_string_5)}")